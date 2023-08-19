import requests
from service_func import download_images
import os
import argparse
from dotenv import load_dotenv


def get_urls_from_spacex(id: str) -> list:
    url = 'https://api.spacexdata.com/v5/launches/{}'.format(id)

    response = requests.get(url)
    response.raise_for_status()

    if id:
        return list(response.json()['links']['flickr']['original'])

    for launch in response.json():
        if not launch['links']['flickr']['original']:
            return list(launch['links']['flickr']['original'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "id",
        nargs='?',
        default='',
        help="download specific launch id"
    )
    args = parser.parse_args()
    id = args.id

    espacex_urls = get_urls_from_spacex(id)
    download_images(espacex_urls, os.getenv('CATALOG'))


if __name__ == '__main__':
    load_dotenv()
    main()
