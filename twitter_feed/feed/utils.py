from twitter_feed.feed.twitter_api.feed import TwitterFeed


def get_feed(query=""):
    twitter_feed = TwitterFeed(query=query)
    return twitter_feed.get_feed()
