from django.core.management.base import NoArgsCommand,CommandError
from TweededBadger import local_settings
from blog.models import Post,PostType
from pprint import pprint
import jsonpickle
# from TwitterAPI import TwitterAPI
# import tweepy
import time

from twitter import *

class Command(NoArgsCommand):
    # args =
    help = 'Gets latest Twitter stuff'

    def handle_noargs(self,**options):
        # self.api = TwitterAPI(consumer_key=local_settings.TWITTER_CONSUMER_KEY,
        #                       consumer_secret=local_settings.TWITTER_CONSUMER_SECRET,
        #                       access_token_key=local_settings.TWITTER_ACCESS_TOKEN_KEY,
        #                       access_token_secret=local_settings.TWITTER_ACCESS_TOKEN_SECRET)
        # r = self.api.request('search/tweets', {'q':'pizza'})
        # for item in r.get_iterator():
        #     print item
        # auth = tweepy.OAuthHandler(local_settings.TWITTER_CONSUMER_KEY, local_settings.TWITTER_CONSUMER_SECRET)
        # auth.set_access_token(local_settings.TWITTER_ACCESS_TOKEN_KEY, local_settings.TWITTER_ACCESS_TOKEN_SECRET)
        # api = tweepy.API(auth)
        # print api.me().name
        # t = Twitter(
        #     auth=OAuth(local_settings.TWITTER_ACCESS_TOKEN_KEY, local_settings.TWITTER_ACCESS_TOKEN_SECRET,
        #                local_settings.TWITTER_CONSUMER_KEY, local_settings.TWITTER_CONSUMER_SECRET)
        #    )
        # tl = t.statuses.user_timeline(screen_name='tweededbadger',count=5)
        # # tl = t.statuses.friends_timeline(id="tweededbadger")
        # pprint(tl)
        self.pt = PostType.objects.get(slug='twitter')
        self.login()
        self.get_tweets()
    def login(self):
        self.twitter_connection = Twitter(
            auth=OAuth(local_settings.TWITTER_ACCESS_TOKEN_KEY, local_settings.TWITTER_ACCESS_TOKEN_SECRET,
                       local_settings.TWITTER_CONSUMER_KEY, local_settings.TWITTER_CONSUMER_SECRET)
           )
    def get_tweets(self):
        tweets = self.twitter_connection.statuses.user_timeline(screen_name='tweededbadger',count=5)
        for tweet in tweets:
            if not self.check_if_saved(tweet):
                # pprint(tweet)
                # print tweet['text']
                # print type(tweet['created_at'])
                # print time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
                self.save(tweet)
            else:
                print "Already saved: "+tweet['text'].encode('utf-8')
    def save(self,tweet):
        tweet_time = time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
        ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
        # if tweet['entities']['media'][0]['media_url']:
        if 'media' in tweet['entities']:
            image = tweet['entities']['media'][0]['media_url']
        else:
            image = None
        p = Post(title=tweet['text'],
             # created=tweet['created_at'],
             created=ts,
             external_link='https://twitter.com/iamdevloper/status/'+tweet['id_str'],
             post_type=self.pt,
             external_data=jsonpickle.encode(tweet),
             external_image=image)
        p.save()
        # print "Saved: "+tweet['text']
        pprint(tweet['text'].encode('utf-8'))
    def check_if_saved(self,tweet):
        try:
            p = Post.objects.get(title=tweet['text'])
            return True
        except:
            return False

