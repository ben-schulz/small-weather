import tweepy

from smallweather.auth import oauth1a


def get_api_instance( consumer_token, consumer_secret ):

    redirect_url, auth_handler = oauth1a(
        consumer_token, consumer_secret )

    request_token = auth_handler.request_token

    return tweepy.API( auth_handler )
