import tweepy
import os, sys
import urllib

from dotenv import load_dotenv

load_dotenv()

def init():
  auth = tweepy.OAuthHandler(os.getenv('API_KEY'), os.getenv('API_KEY_SECRET'))
  auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))

  urls = sys.argv[1::]
  print(urls)

  api = tweepy.API(auth)

  for url in urls:

    tweet_id = url[url.index("status") + 7::]
    tweet_data = api.get_status(id=tweet_id)

    media = tweet_data.extended_entities['media']
    hashtags = tweet_data.entities['hashtags']
    media_urls = []
    index = 1;
    for item in media:
      media_urls.append(item['media_url_https'])
      download_image(item['media_url_https'] + ':orig', tweet_data.user.screen_name + '-' + tweet_data.id_str + '-0' + str(index))
      index += 1
      pass

    print(tweet_data.user.name + ': ' + tweet_data.id_str)
    pass

def download_image(img_url, filename):
  downloaded_file_path = ''
  extension = img_url[img_url.rfind('.'):img_url.rfind(':')]
  try:
    urllib.request.urlretrieve(img_url, filename + extension)
  except Exception as e:
    print(image_on_web.headers['Content-Type'])
    print('error downloading image ' + img_url + ', ' + e)
    return False
  return True



if __name__ == '__main__':
  init()