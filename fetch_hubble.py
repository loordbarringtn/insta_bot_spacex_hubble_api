import requests
import os

IMAGE_COLLECTION='spacecraft'
IMAGE_DIRECTORY= 'images/'

def getting_image_url_from_image_id(image_id):
    response = requests.get(f'http://hubblesite.org/api/v3/image/{image_id}', verify=False)
    response.raise_for_status()
    data = response.json()
    data_from_dictionary = data["image_files"]
    specific_photo=data_from_dictionary[-1]
    image_url=specific_photo['file_url']
    return image_url

def getting_file_extension(image_id):
    extension_from_url_name =getting_image_url_from_image_id(image_id).split('.')[-1]
    return extension_from_url_name

def save_hubble_images(image_id,IMAGE_DIRECTORY):
    os.makedirs(IMAGE_DIRECTORY,exist_ok=True)
    image_full_web_adress = '{}'.format('https:') + getting_image_url_from_image_id(image_id)
    file_name = '{}{}{}'.format('hubble', image_id, '.') + getting_file_extension(image_id)
    complete_filename = os.path.join(IMAGE_DIRECTORY, file_name)
    response = requests.get(image_full_web_adress, verify=False)
    response.raise_for_status()
    with open(complete_filename, 'wb') as f:
          f.write(response.content)
          f.close()

def download_hubble_collections(IMAGE_COLLECTION,IMAGE_DIRECTORY):
    url = f'http://hubblesite.org/api/v3/images?page=all&collection_name={IMAGE_COLLECTION}'
    response = requests.get(url)
    response.raise_for_status()
    response_data = response.json()
    for spaceship in (response_data):
          image_full_web_adress = 'https:' + getting_image_url_from_image_id(spaceship['id'])
          file_name = image_full_web_adress.split("/")[-1]
          complete_filename = os.path.join(IMAGE_DIRECTORY, file_name)
          response = requests.get(image_full_web_adress, verify=False)
          response.raise_for_status()
          with open(complete_filename, 'wb') as f:
                 f.write(response.content)
                 f.close()

if __name__ == '__main__':
    try:
       download_hubble_collections(IMAGE_COLLECTION,IMAGE_DIRECTORY)
    except requests.exceptions.HTTPError as err:
       print(err)
    except IOError as e:
       print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except OSError as error:
       print("OS error: {0}".format(error))
