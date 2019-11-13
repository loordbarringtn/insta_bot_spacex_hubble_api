import requests
import os

SPACEX_URL = "https://api.spacexdata.com/v3/launches/latest"
IMAGE_DIRECTORY= 'images/'

def spacex_save_file(content,IMAGE_DIRECTORY):
    os.makedirs(IMAGE_DIRECTORY,exist_ok=True)
    filename = content.split("/")[-1]
    complete_filename = os.path.join(IMAGE_DIRECTORY, filename)
    response = requests.get(content)
    response.raise_for_status()
    with open(complete_filename, 'wb') as f:
          f.write(response.content)
          f.close()

def fetch_spacex_last_launch(SPACEX_URL):
    response = requests.get(SPACEX_URL)
    response.raise_for_status()
    data=response.json()
    photo_filename=data['links']['flickr_images']
    for i,b in enumerate (photo_filename):
        spacex_save_file(b,IMAGE_DIRECTORY)

if __name__ == '__main__':
    try:
      fetch_spacex_last_launch(SPACEX_URL)
    except requests.exceptions.HTTPError as err:
      print(err)
    except OSError as error:
      print("OS error: {0}".format(error))
    except IOError as e:
      print("I/O error({0}): {1}".format(e.errno, e.strerror))
