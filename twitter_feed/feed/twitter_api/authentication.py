import requests
from django.conf import settings


class TwitterAuthentication:

    auth_url = "https://api.twitter.com/oauth2/token"
    data = {
        "grant_type": "client_credentials"
    }
    auth = (settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET)

    def fetch_token(self):
        request = requests.post(self.auth_url, auth=self.auth, data=self.data)
        return request.status_code, request.json()
