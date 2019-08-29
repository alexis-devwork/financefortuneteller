import tweepy

class Tweeter:

    def __init__(self,CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET):
        self.CONSUMER_KEY = CONSUMER_KEY.strip()
        self.CONSUMER_SECRET = CONSUMER_SECRET.strip()
        self.ACCESS_KEY = ACCESS_KEY.strip()
        self.ACCESS_SECRET = ACCESS_SECRET.strip()
        self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        self.auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)
        self.api = tweepy.API(self.auth)

    def tweet(self,txt):
        self.api.update_status(txt)

#tw = Tweeter("credentials.txt")
#tw.tweet("I want to help you understand and predict the world!")
#tw.tweet(" " + '\ud83e\udde9'.encode('utf-16', 'surrogatepass').decode('utf-16'))
#tw.tweet("Hi "+'\U0001f604'.encode('utf-8').decode('utf-8'))
#tw.tweet("Hi "+'\U0001F504'.encode('utf-8').decode('utf-8')+" Reversed")
