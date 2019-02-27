from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import csv
import sys
import time

#consumer key, consumer secret, access token, access secret.
ckey="hpbARu5lJlozST82JEdXYcaS7"
csecret="JpfbXATmdNPz6yIhFwmVU1mGU28QTICCuYkfqGibb25HV4x4VK"
atoken="1094363214043889665-UohVaHgV89P7OtSgUlWq6QJ6q30Yu1"
asecret="mz0RhOmUHN2ISAFcE3j0bOwZVxoAy5x5Ccn8RAiqYrRRI"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

#emoji may give trouble when printing (not saving) so creating a translation table
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

f = open('tweepy_tweets.csv', 'w')
writer = csv.writer(f)
writer.writerow(["id","created_at","text"])

alltweets = tweepy.Cursor(api.search, q='the lego movie').items()
for tweet in alltweets:
 #print(str(tweet).translate(non_bmp_map))
 outtweets = [tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")]
 writer.writerow(outtweets)
 print(outtweets)
 time.sleep(2)
f.close()