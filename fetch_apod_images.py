import requests
import os
from service_func import download_images
from dotenv import load_dotenv


def get_urls_from_apod(count: int, api_key: str) -> list:
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': count
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    urls_images = []
    for img in response.json():
        urls_images.append(img['url'])

    return urls_images


def main():
    urls_images = get_urls_from_apod(
        10,
        os.getenv('NASA_API_KEY')
    )
    download_images(urls_images, os.getenv('CATALOG'))


if __name__ == '__main__':
    load_dotenv()
    main()
