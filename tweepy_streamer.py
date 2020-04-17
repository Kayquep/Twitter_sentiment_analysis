from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials


class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        "Function to handle the authentication and the connection to Twitter Streamiing API"
        listener = StdOutListener()
        auth = OAuthHandler(twitter_credentials.consumer_key,
                            twitter_credentials.consumer_secret)
        auth.set_access_token(twitter_credentials.access_token,
                              twitter_credentials.access_token_secret)

        stream = Stream(auth, listener)

        stream.filter(track=hash_tag_list)


class StdOutListener(StreamListener):
    """
    This is a basic listener class that just prints received tweets to stdout.
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
