from instabot import Bot
import requests
import os
from dotenv import load_dotenv
PROCESSED_IMAGES='processed_images/'

def insta_bot(PROCESSED_IMAGES):
    load_dotenv()
    bot = Bot()
    instagram_username= os.getenv("username")
    instagram_password= os.getenv("password")
    bot.login(username=instagram_username, password=instagram_password)
    for file in os.listdir(PROCESSED_IMAGES):
        caption=file.split('.')[0]
        bot.upload_photo(os.path.join(PROCESSED_IMAGES,file),caption=caption)

if __name__ == '__main__':
    insta_bot(PROCESSED_IMAGES)
