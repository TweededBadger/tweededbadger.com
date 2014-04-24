from django.contrib.auth import login
from django.core.management.base import NoArgsCommand,CommandError
from django.core.exceptions import ObjectDoesNotExist
from TweededBadger import local_settings
from blog.models import Post,PostType
import praw
from pprint import pprint
from django.utils import timezone
import jsonpickle
import datetime

class Command(NoArgsCommand):
    # args =
    help = 'Gets latest Reddit stuff'

    def handle_noargs(self,**options):
        self.reddit_u = local_settings.REDDIT_LOGIN
        self.reddit_p = local_settings.REDDIT_PASSWORD
        self.stdout.write('Hello there ' + self.reddit_u)
        try:
            self.pt = PostType.objects.get(slug='reddit')
        except ObjectDoesNotExist:
            self.create_reddit_postype()
        self.login()
        self.get_saved()
        # self.test()

    def create_reddit_postype(self):
        self.pt = PostType(name="Reddit",slug="reddit")
        self.pt.save()


    def login(self):
        self.r = praw.Reddit(user_agent='HoneybadgerUK Blog')
        self.r.login(self.reddit_u,self.reddit_p)

    def get_saved(self):
        liked = self.r.user.get_liked()
        # print len(saved)
        for like in liked:
            # pprint(vars(like))
            # pprint(like.title)
            # pprint(jsonpickle.encode(like))
            # pprint(jsonpickle.encode(like))
            if not self.check_if_saved(like):
                self.save(like)
            else:
                print like.title + " already saved"
                break
        # vars(saved)
    def save(self,like):
        p = Post(title=like.title,
                 created=datetime.datetime.fromtimestamp(int(like.created_utc)),
                 external_link=like.permalink,
                 post_type=self.pt,
                 external_data=jsonpickle.encode(like)
        )
        p.save()
    def check_if_saved(self,like):
        try:
            p = Post.objects.get(title=like.title)
            return True
        except:
            return False
    def test(self):
        pt = PostType.objects.get(slug='reddit')
        pprint(pt);
        p = Post(title="test",created=timezone.now(),post_type=pt)
        p.save()
