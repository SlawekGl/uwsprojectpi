from twython import TwythonStreamer

from twitter_auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
#            username = data['user']['screen_name']
            tweet = data['text']
#            location = data['coordinates']
#            print (data['text'].encode('utf-8'))
#            print("@%s: %s %s" % (username, tweet, location))
            print(tweet)
    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        #self.disconnect()

stream = MyStreamer(consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
stream.statuses.filter(track='test14')
