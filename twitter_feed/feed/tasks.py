from twitter_feed.celery import app
from twitter_feed.feed.models import SearchResultsMeta, SearchResults, QueryEntry
from twitter_feed.feed.utils import get_feed


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, collect_tweet.s(), name='add every 60')


@app.task
def collect_tweet():
    query_list = QueryEntry.objects.all().values_list("query", flat=True)
    for query in query_list:
        feed = get_feed(query=query)
        search_metadata = feed.get("search_metadata", "")
        statuses = feed.get("statuses", [])

        meta = SearchResultsMeta.objects.create(search_metadata=search_metadata)

        for status in statuses:
            SearchResults.objects.create(search_metadata=meta, search_data=status)

    return query_list
