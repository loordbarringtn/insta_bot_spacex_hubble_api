import requests
import os

IMAGE_COLLECTION='spacecraft'
IMAGE_DIRECTORY= 'images/'

def getting_image_url_from_image_id(image_id):
    try:
       response = requests.get(f'http://hubblesite.org/api/v3/image/{image_id}', verify=False)
       response.raise_for_status()
    except requests.exceptions.HTTPError as err:
       print (err)
    data = response.json()
    select_from_dictionary = data["image_files"]
    specific_photo=select_from_dictionary[-1]
    image_adress=specific_photo['file_url']
    return image_adress


def make_file_extension(image_id):
    extension_from_url_name =getting_image_url_from_image_id(image_id).split('.')[-1]
    return extension_from_url_name


def hubble_save_file(image_id,IMAGE_DIRECTORY):
    try:
      if not os.path.exists(IMAGE_DIRECTORY):
         os.mkdir(IMAGE_DIRECTORY)
    except OSError:
        print("Creation of the directory %s failed")
    image_full_web_adress = 'https:'+ getting_image_url_from_image_id(image_id)
    file_name='hubble' + str(image_id)+'.'+make_file_extension(image_id)
    complete_filename = os.path.join(IMAGE_DIRECTORY, file_name)
    try:
       response = requests.get(image_full_web_adress, verify=False)
       response.raise_for_status()
    except requests.exceptions.HTTPError as err:
       print (err)
    try:
       with open(complete_filename, 'wb') as f:
          f.write(response.content)
          f.close()
    except IOError as e:
          print("I/O error({0}): {1}".format(e.errno, e.strerror))


def hubble_collections_instant_download(IMAGE_COLLECTION,IMAGE_DIRECTORY):
    url = f'http://hubblesite.org/api/v3/images?page=all&collection_name={IMAGE_COLLECTION}'
    response = requests.get(url)
    response.raise_for_status()
    response_data = response.json()
    for spaceship in (response_data):
          image_full_web_adress = 'https:' + getting_image_url_from_image_id(spaceship['id'])
          file_name = image_full_web_adress.split("/")[-1]
          print(file_name)
          complete_filename = os.path.join(IMAGE_DIRECTORY, file_name)
          try:
             response = requests.get(image_full_web_adress, verify=False)
             response.raise_for_status()
          except requests.exceptions.HTTPError as err:
             print (err)
          try:
             with open(complete_filename, 'wb') as f:
                 f.write(response.content)
                 f.close()
          except IOError as e:
              print("I/O error({0}): {1}".format(e.errno, e.strerror))

if __name__ == '__main__':
    hubble_collections_instant_download(IMAGE_COLLECTION,IMAGE_DIRECTORY)
