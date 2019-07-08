# small-weather

## getting started

set up your environment:

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

copy 'config_template.ini' to 'config.ini' and fill in
your consumer keys, as visible at: 'https://developer.twitter.com/en/apps/your_app_id'.

run:

```
python go.py
```

to see if it's working. (you should see a big blob of tweet stuff).

## and then?

this is currently just a crude wrapper around Tweepy;
to do something more interesting, see the docs for that:

http://docs.tweepy.org/en/v3.7.0/getting_started.html