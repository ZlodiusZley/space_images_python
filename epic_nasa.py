import requests
import os
from datetime import datetime


def download_image(url, path, params=None):
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        with open(path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Ошибка при загрузке изображения. Код состояния: {response.status_code}")

def get_epic_nasa(nasa_api_key, save_path, links_count):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    
    params = {
        'api_key': nasa_api_key,
        'count': links_count
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        nasa_epic_images = response.json()

        for nasa_epic_image in nasa_epic_images:
            file_name = nasa_epic_image['image']
            epic_image_date = nasa_epic_image['date']
            epic_image_date = datetime.fromisoformat(epic_image_date).strftime("%Y/%m/%d")
            link_path = f'https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{file_name}.png' 
            path = os.path.join(save_path, f"{file_name}.png")

            os.makedirs(save_path, exist_ok=True)

            download_image(link_path, path, params)
    else:
        print(f"Не удалось получить изображения NASA EPIC. Код состояния: {response.status_code}")


if __name__ == "__main__":
    api_key = 'A8R6BXTgEREcdcHDL5EtpCvGHa8JFkj1g6uRgcag' # спрятать ключ 
    save_path = 'images'
    links_count = 5

    get_epic_nasa(api_key, save_path, links_count)
