from django.urls import path

from twitter_feed.feed.views import TwitterFeedEnableAPIView, TwitterFeedDisableAPIView, TweetListAPIView

app_name = "twitter_feed.feed"

urlpatterns = [
    path('', TweetListAPIView.as_view(), name="tweet_list"),
    path('enable/', TwitterFeedEnableAPIView.as_view(), name="query_enable"),
    path('disable/', TwitterFeedDisableAPIView.as_view(), name="query_disable"),
]
