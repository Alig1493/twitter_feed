from django.contrib import admin

# Register your models here.
from twitter_feed.feed.models import SearchResultsMeta, QueryEntry, SearchResults

admin.site.register(QueryEntry)
admin.site.register(SearchResultsMeta)
admin.site.register(SearchResults)
