from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.
class QueryEntry(models.Model):
    query = models.CharField(max_length=512)


class SearchResultsMeta(models.Model):
    search_metadata = JSONField()


class SearchResults(models.Model):
    search_metadata = models.ForeignKey(SearchResultsMeta, related_name="search_results", on_delete=models.CASCADE)
    search_data = JSONField()
