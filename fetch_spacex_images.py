import requests
from service_func import download_images
import os
from dotenv import load_dotenv
load_dotenv()


def get_urls_from_spacex() -> list:
    url = 'https://api.spacexdata.com/v5/launches/'

    response = requests.get(url)
    response.raise_for_status()

    for launch in response.json():
        if len(launch['links']['flickr']['original']) > 0:
            spacex_urls = list(launch['links']['flickr']['original'])
            break

    return spacex_urls


def main():
    espacex_urls = get_urls_from_spacex()
    download_images(espacex_urls, os.getenv('CATALOG'))


if __name__ == '__main__':
    main()
