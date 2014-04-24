from django.test import TestCase
from django.core import management

# class RedditTest(TestCase):
#     def test_getRedditPosts(self):
#         management.call_command("get_reddit")
class TwitterTest(TestCase):
    def test_getTwitterPosts(self):
        management.call_command("get_twitter")