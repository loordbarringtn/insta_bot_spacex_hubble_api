from instabot import Bot
import requests
import os
from dotenv import load_dotenv
PROCESSED_IMAGES='processed_images/'

def insta_bot():
    load_dotenv()
    bot = Bot()
    instagram_username= os.getenv("username")
    instagram_password= os.getenv("password")
    bot.login(username=instagram_username, password=instagram_password)
    files=os.listdir(PROCESSED_IMAGES)
    for file in files:
        caption=file.split('.')[0]
        bot.upload_photo(os.path.join(PROCESSED_IMAGES,file),caption=caption)

if __name__ == '__main__':
    insta_bot()
