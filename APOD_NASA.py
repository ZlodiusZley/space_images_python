import requests
import os
from urllib.parse import urlparse, unquote
from datetime import datetime

def extract_extension_from_link(link):
    decoded_link = unquote(link)
    parsed_link = urlparse(decoded_link)
    path, fullname = os.path.split(parsed_link.path)
    file_extension_path = os.path.splitext(fullname)
    file_name, extension = file_extension_path
    return extension, file_name

def getting_images(nasa_api_key, folder_name, links_count):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key': nasa_api_key,
        'count': links_count,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    nasa_images = response.json()
    for image_nasa in nasa_images[:links_count]:
        if image_nasa.get("media_type") == "image":
            if image_nasa.get("hdurl"):
                nasa_link_image = image_nasa["hdurl"]
            else:
                nasa_link_image = image_nasa["url"]

            file_extension, file_name = extract_extension_from_link(nasa_link_image)
            path = os.path.join(folder_name, f'{file_name}{file_extension}')
            response = requests.get(nasa_link_image)
            response.raise_for_status()
            with open(path, 'wb') as file:
                file.write(response.content)

if __name__ == "__main__":
    nasa_api_key = 'A8R6BXTgEREcdcHDL5EtpCvGHa8JFkj1g6uRgcag'
    save_path = 'images'
    getting_images(nasa_api_key, save_path, 30)
