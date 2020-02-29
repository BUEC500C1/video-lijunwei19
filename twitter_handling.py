import tweepy as tp 
import configparser
import json  
import time
import pprint as pp  
import image_processing as IMP

class twitter_feed_catching():

  def __init__(self, path):
    # getting twitter api keys from keys configuration file
    config = configparser.ConfigParser()
    config.read(path)
    consumer_key = config.get('auth', 'consumer_key').strip()
    consumer_secret = config.get('auth', 'consumer_secret').strip()
    access_token = config.get('auth', 'access_token').strip()
    access_secret = config.get('auth', 'access_secret').strip()

    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token = (access_token, access_secret) 

    self.api = tp.API(auth)
    self.content = []

  def get_user_pic(self, username):
    # getting the users' picture_url
        try:
            u = self.api.get_user(username)
            return u.profile_image_url_https
        except tp.error.TweepError:
            return ""

  
  def get_users_tweets(self, username):
        try:
            tweets = self.api.user_timeline(screen_name=username, count=20, include_rts=True, result_type="recent",
                                    include_entities=True,
                                    tweet_mode='extended',
                                    lang="en")
            # get tweets content save it self.content 
            for tweet in tweets:
              self.content.append(tweet.full_text)

            return tweets
        except tp.error.TweepError:
            return ""

  def save_json(self,username):
          json_tweets = json.dumps(self.content,indent = 4)
          path = 'Json/'+username+'.json'
          with open(path, 'w') as outfile:
            outfile.write(json_tweets)  

# def main():
#   a = twitter_feed_catching("keys")
#   username = input("twitter_ID: ")
#   profile_url = a.get_user_pic(username)
#   print(profile_url)
#   tweets = a.get_users_tweets(username)
#   a.save_json(username)
#   # IMP.create_images(username, profile_url, tweets)

# if __name__ == '__main__':
#   main()