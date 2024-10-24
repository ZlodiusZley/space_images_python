import requests
import os
from urllib.parse import urlparse, unquote
from datetime import datetime

def getting_images(launch_id): 
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    images_url = response.json()["links"]["flickr"]["original"]
    return images_url 


def fetch_spacex_last_launch(images_url, save_path):
    for image in images_url:
        response = requests.get(image)
        response.raise_for_status()

        file_name = image.split("/")[-1]  
        full_save_path = os.path.join(save_path, file_name)

        with open(full_save_path , 'wb') as file:
            file.write(response.content)


if __name__ == "__main__":
    launch_id = "5eb87d42ffd86e000604b384"
    save_path = 'images'
    images_url = getting_images(launch_id)
    fetch_spacex_last_launch(images_url, save_path)

