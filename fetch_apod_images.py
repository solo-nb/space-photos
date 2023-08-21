import requests
import os
from service_func import download_image
from dotenv import load_dotenv


NUMBER_OF_IMG_TO_DOWNLOAD = 10


def get_urls_from_apod(count: int, api_key: str) -> list:
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': count
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    urls_images = [img['url'] for img in response.json()]

    return urls_images


def main():
    load_dotenv()
    urls_images = get_urls_from_apod(
        NUMBER_OF_IMG_TO_DOWNLOAD,
        os.getenv('NASA_API_KEY')
    )
    for url in urls_images:
        download_image(url, os.getenv('CATALOG'))


if __name__ == '__main__':
    main()
