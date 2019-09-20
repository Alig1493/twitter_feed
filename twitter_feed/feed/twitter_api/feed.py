import requests
from django.core.cache import cache
from rest_framework import status
from rest_framework.exceptions import APIException

from twitter_feed.feed.twitter_api.authentication import TwitterAuthentication


class TwitterFeed:

    url = "https://api.twitter.com/1.1/search/tweets.json"
    headers = {
        "authorization": ""
    }
    params = {
        "q": ""
    }
    access_token = ""
    query = ""

    def __init__(self, query="serverless"):
        self.twitter_auth = TwitterAuthentication()
        self.cache_key = "access_token"
        self.set_feed_request_params(query=query)

    def fetch_token(self):
        if cache.get(self.cache_key):
            return cache.get(self.cache_key)

        status_code, json_data = self.twitter_auth.fetch_token()
        if status_code == status.HTTP_200_OK:
            cache.set(self.cache_key, json_data.get("access_token"))
            return json_data.get("access_token")
        raise APIException(json_data)

    def set_feed_request_params(self, query):
        self.access_token = self.fetch_token()
        self.query = query
        self.set_headers()
        self.set_params()

    def set_headers(self):
        self.headers.update(authorization=f"Bearer {self.access_token}")

    def set_params(self):
        self.params.update(q=self.query)

    def get_feed(self):
        request = requests.get(self.url, headers=self.headers, params=self.params)
        return request.json()
