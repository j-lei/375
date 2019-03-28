from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import sys
import json

ckey="hpbARu5lJlozST82JEdXYcaS7"
csecret="JpfbXATmdNPz6yIhFwmVU1mGU28QTICCuYkfqGibb25HV4x4VK"
atoken="1094363214043889665-UohVaHgV89P7OtSgUlWq6QJ6q30Yu1"
asecret="mz0RhOmUHN2ISAFcE3j0bOwZVxoAy5x5Ccn8RAiqYrRRI"

TWEET_COUNT = 2

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15*60)

# assumes actor_list has no duplicates
def query_runner(api):
    actor_list = []
    tweets_by_actors = {}
    
    with open('test_actors.txt') as actor_file:
        for line in actor_file:
            actor_list.append(line.strip())
    print(actor_list)
    
    for actor in actor_list:
        tweet_list = []
        cursor = tweepy.Cursor(api.search, q=actor, lang='en',                  tweet_mode='extended').items(TWEET_COUNT)
        
        for tweet in limit_handled(cursor):
            if hasattr(tweet, 'text'):
                contents = tweet.text
            else:
                contents = tweet.full_text
            datetime = tweet.created_at
            tweet_tuple = datetime, contents
            tweet_list.append(tweet_tuple)
        
        tweets_by_actors[actor] = tweet_list
    
    print(tweets_by_actors)

def main():
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api = tweepy.API(auth)

    query_runner(api)
main()