import twitter_handling as tw
import image_processing as imagp
import ImageToVideo as ITV
import configparser
import tweepy as tp 
import os 
import pytest

def test_files():
  assert os.path.exists('keys')
  assert os.path.exists('main.py')
  assert os.path.exists('twitter_handling.py')
  assert os.path.exists('ImageToVideo.py')
  assert os.path.exists('image_processing.py')
  assert os.path.exists('video/')
  assert os.path.exists('processed_imgs/')
  assert os.path.exists('character_type/arial.ttf')

def test_api_keys():
  config = configparser.ConfigParser()
  config.read('keys')

  auth = tp.OAuthHandler(config.get('auth', 'consumer_key').strip(), 
                          config.get('auth', 'consumer_secret').strip())
  auth.set_access_token = (config.get('auth', 'access_token').strip(),
                           config.get('auth', 'access_secret').strip()) 
  api = tp.API(auth)
  try:
    u = api.get_user("BU")
    assert os.path.exists('processed_imgs/BU_img1.png')
  except tp.error.TweepError:
    assert False



def test_image2video():
  IDs = ['BU']
  for ID in IDs:
    path = "video/" + ID + "better.mp4"
    path1 = "video/" + ID + "normal.avi"
    if (os.path.exists(path)):
       os.remove(path)
    if (os.path.exists(path1)):
       os.remove(path1)
    ITV.imgToVideo(ID) 
    assert os.path.exists(path) 


