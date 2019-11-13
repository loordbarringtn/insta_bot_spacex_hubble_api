import requests
import os

SPACEX_URL = "https://api.spacexdata.com/v3/launches/latest"
IMAGE_DIRECTORY= 'images/'

def spacex_save_file(content,IMAGE_DIRECTORY):
    try:
      if not os.path.exists(IMAGE_DIRECTORY):
         os.mkdir(IMAGE_DIRECTORY)
    except OSError:
        print("Creation of the directory %s failed")
    filename = content.split("/")[-1]
    complete_filename = os.path.join(IMAGE_DIRECTORY, filename)
    try:
       response = requests.get(content)
       response.raise_for_status()
    except requests.exceptions.HTTPError as err:
       print (err)
    try:
       with open(complete_filename, 'wb') as f:
          f.write(response.content)
          f.close()
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))

def fetch_spacex_last_launch(SPACEX_URL):
    try:
       response = requests.get(SPACEX_URL)
       response.raise_for_status()
    except requests.exceptions.HTTPError as err:
       print (err)
    data=response.json()
    photo_filename=data['links']['flickr_images']
    for i,b in enumerate (photo_filename):
        spacex_save_file(b,IMAGE_DIRECTORY)

if __name__ == '__main__':
    fetch_spacex_last_launch(SPACEX_URL)

