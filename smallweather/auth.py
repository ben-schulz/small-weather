import tweepy

def oauth1a( consumer_token, consumer_secret ):

    auth = tweepy.OAuthHandler( consumer_token, consumer_secret )

    try:
        redirect_url = auth.get_authorization_url()
    
    except tweepy.TweepError as ex:
        print( f'Failed to get request token: {ex}' )
        raise

    return redirect_url, auth
