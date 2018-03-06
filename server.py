# -*- coding: utf-8 -*-

import requests
import os
import tweepy
import shutil
import PIL
import pip
import aggdraw
import urllib
import json
import random
import dropbox





def tweet(file,text):
  # Twitter authentication
  auth = tweepy.OAuthHandler(os.environ['C_KEY'], os.environ['C_SECRET'])
  auth.set_access_token(os.environ['A_TOKEN'], os.environ['A_TOKEN_SECRET'])
  api = tweepy.API(auth)

  api.update_with_media(file,text)
  
  '''Here is the Part That uses PIL'''
def tweet_image():
  url = 'your image url'
    response = requests.get(url, stream=True)
     #you shold be able to specify a path, check glitch support for writing to ASSETS or to .tmp folder
    with open('img.jpg', 'wb') as out_file:
      shutil.copyfileobj(response.raw, out_file)
      from PIL import Image, ImageDraw, ImageFile
      ImageFile.LOAD_TRUNCATED_IMAGES = True

      im = Image.open("img.jpg")
      
      
      
      
      url2 = 'your font url'
    response = requests.get(url2, stream=True)
     #you shold be able to specify a path, check glitch support for writing to ASSETS or to .tmp folder
    with open('font.ttf', 'wb') as out_file:
      shutil.copyfileobj(response.raw, out_file)
      
      '''Something to Post'''
      
      municipalities_response = requests.get('https://botwiki.org/api/corpora/data/geography/canadian_municipalities.json')
      the_municipalities = municipalities_response.json()
      municipalities_list = []
  
      for f in the_municipalities["municipalities"]:
        for k, v in f.iteritems():
          municipalities_list.append(v)

      n = random.randint(0,len(municipalities_list))
      the_municipality = municipalities_list[n]

      plant_response = requests.get('https://botwiki.org/api/corpora/data/plants/plants.json')
      the_plants = plant_response.json()
      plant_list = []

      for p in the_plants['instruments']:
        plant_list.append(p['name'])

      m = random.randint(0,len(plant_list))
      the_plant = plant_list[m]

      '''Here is the Part That Uses Aggdraw'''
      font = aggdraw.Font((255, 255, 255), "/app/font.ttf")
      d = aggdraw.Draw(im)
      p = aggdraw.Pen((255, 255, 255), 100)
      b = aggdraw.Brush((255, 255, 255))
      #d.ellipse((0, 0, 500, 500), p, b)
      #d.ellipse((0, 500, 500, 0), p, b)
      d.text((100, 100), "suck on my %s , you %s " % (the_municipality,the_plant), font)
      d.flush()
      del d
      im.save('/app/img.jpg')
      del response
    filename = 'img.jpg'
    text = "Yes!"
    
    return filename,text

if __name__ == "__main__":
  image,text = tweet_image()
  tweet(image,text)
  