import os
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

cursor = tweepy.Cursor( api.user_timeline, id='wicked_sleep' )

# this is just a sanity check,
# to see if it's working
print( next( iter( cursor.items( 10 ) ) ) )

