from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import testProj.sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="tqpifMEzZI5qjDUvxma7UjOoY"
csecret="F5l6SR3pbl5adqq5pGk6QszNHRGaCnX7eqsiwrAljoOJAqTi8p"
atoken="3990154933-5ovIIIBfZhZQe97VERhsEwv0qzG43evn9nfbOvN"
asecret="UPDov2KR5jX9OZn2MOX5zFlKca1JWZkDzCXBmxV8a2iFG"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence * 100 >= 80:
            output = open("twitter-out.txt", "a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])