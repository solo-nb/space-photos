import requests
from service_func import download_image
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
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='This script downloads photos from spacex launches'
    )
    parser.add_argument(
        "id",
        nargs='?',
        default='',
        help="Download specific launch id. If not specified, \
existing photos of the last launch are downloaded"
    )
    args = parser.parse_args()
    id = args.id

    espacex_urls = get_urls_from_spacex(id)
    for url in espacex_urls:
        download_image(url, os.getenv('CATALOG'))


if __name__ == '__main__':
    main()
