# Create your views here.
from rest_framework.generics import CreateAPIView, ListAPIView

from twitter_feed.feed.models import SearchResultsMeta
from twitter_feed.feed.serializers import QuerySerializer, RemoveQuerySerializer, SearchResultsMetaSerializer


class TwitterFeedEnableAPIView(CreateAPIView):
    serializer_class = QuerySerializer


class TwitterFeedDisableAPIView(TwitterFeedEnableAPIView):
    serializer_class = RemoveQuerySerializer


class TweetListAPIView(ListAPIView):
    serializer_class = SearchResultsMetaSerializer
    queryset = SearchResultsMeta.objects.all()
