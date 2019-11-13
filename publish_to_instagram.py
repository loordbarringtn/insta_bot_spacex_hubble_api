import os
import requests
from instabot import Bot
from dotenv import load_dotenv
from PIL import Image

from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import hubble_collections_instant_download
from insta_bot import instabot

SPACEX_URL = "https://api.spacexdata.com/v3/launches/latest"
PROCESSED_IMAGES='processed_images/'
IMAGE_COLLECTION='spacecraft'
IMAGE_DIRECTORY= 'images/'


def using_pillow_for_image_resize(IMAGE_DIRECTORY,PROCESSED_IMAGES):
    try:
        if not os.path.exists(PROCESSED_IMAGES):
            os.mkdir(PROCESSED_IMAGES)
    except OSError:
        print("Creation of the directory %s failed")
    for filename in os.listdir(IMAGE_DIRECTORY):
            if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.tif')):
                print("No image file inside this directory")
            else:
                try:
                   image=Image.open(os.path.join(IMAGE_DIRECTORY,filename))
                   resized_image=image.resize((1080,1080))
                   resized_image.save((os.path.join(PROCESSED_IMAGES,filename)))
                   print(image.size)
                except os.error as e:
                    print(e)

def main():
    fetch_spacex_last_launch(SPACEX_URL)
    hubble_collections_instant_download(IMAGE_COLLECTION,IMAGE_DIRECTORY)
    using_pillow_for_image_resize(IMAGE_DIRECTORY, PROCESSED_IMAGES)
    insta_bot()

if __name__ == '__main__':
    main()