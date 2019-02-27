from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import csv
import sys

#consumer key, consumer secret, access token, access secret.
ckey="86o1IyP33QYGCketuZqmHai1R"
csecret="7JYxRSOQJv9oYbFIk09CRmBX3jOazAPwCzHA9cw6Z460PHOIjW"
atoken="1094363214043889665-xuGnzSDEDsL4CL84TtU7MRRysx4p2u"
asecret="WU4t80lKaEfBkzM1JGdjaB67VGe7fsnY5mOC8mEiUB0lz"

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
f.close()