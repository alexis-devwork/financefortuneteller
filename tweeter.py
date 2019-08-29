import tweepy

class Tweeter:

    def __init__(self,credfile):
        filename = open(credfile,'r')
        f = filename.readlines()
        filename.close()
        self.CONSUMER_KEY = f[0].strip()
        self.CONSUMER_SECRET = f[1].strip()
        self.ACCESS_KEY = f[2].strip()
        self.ACCESS_SECRET = f[3].strip()
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
