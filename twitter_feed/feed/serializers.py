from django.conf import settings
from rest_framework import serializers

from twitter_feed.feed.models import QueryEntry, SearchResultsMeta, SearchResults


class QuerySerializer(serializers.ModelSerializer):

    class Meta:
        model = QueryEntry
        fields = "__all__"


class RemoveQuerySerializer(serializers.ModelSerializer):

    class Meta:
        model = QueryEntry
        fields = "__all__"

    def create(self, validated_data):
        query = validated_data.get("query", "")
        if query:
            QueryEntry.objects.filter(query=query).delete()
        return validated_data


class SearchResultsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchResults
        fields = ["search_data"]


class SearchResultsMetaSerializer(serializers.ModelSerializer):
    search_results = SearchResultsSerializer(many=True)

    class Meta:
        model = SearchResultsMeta
        fields = "__all__"
