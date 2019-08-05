import os
import json
import datetime
import configparser

import tweepy

from smallweather import get_api_instance


this_dir = os.path.dirname( os.path.abspath( __file__ ) )
config_path = os.path.join( this_dir, './config.ini' )

if not os.path.exists( config_path ):
    message = f'Make a copy of \'config_template.ini\', '
    'rename to \'config.ini\', '
    'and fill in your consumer token and secret.'

    raise RuntimeError( message )

config = configparser.ConfigParser()
config.read( config_path )

consumer_token = config[ 'twitter_secrets' ][ 'consumer_token' ]
consumer_secret = config[ 'twitter_secrets' ][ 'consumer_secret' ]

api = get_api_instance( consumer_token, consumer_secret )

userid = 'realDonaldTrump'
record_count = 44000
cursor = tweepy.Cursor( api.user_timeline, id=userid, tweet_mode='extended' )

# this is just a sanity check,
# to see if it's working

tweets = iter( cursor.items( record_count ) )

results = []
for t in tweets:
    try:
        d = t._json
        d[ '__retrievedat__' ] = str( datetime.datetime.utcnow() )
        results.append( d )

    except Exception as e:
        print( e )
        break


with open( 'dump.json', 'w' ) as f:
    f.write( json.dumps( results ) )
