from twython import Twython

from twitter_auth import (
      consumer_key,
      consumer_secret,
      access_token,
      access_token_secret
  )

twitter = Twython(
      consumer_key,
      consumer_secret,
      access_token,
      access_token_secret
  )
message = "Test01"
twitter.update_status(status=message)
print("Tweeted: %s" % message)