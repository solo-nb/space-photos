import requests
import os
from datetime import datetime
from service_func import download_images
from dotenv import load_dotenv


def get_urls_from_epic(api_key: str) -> list:
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    epic_urls = []
    for img in response.json():

        date = datetime.strptime(img['date'], "%Y-%m-%d %H:%M:%S")
        epic_urls.append(
            'https://api.nasa.gov/EPIC/archive/natural/{:04}/{:02}/{:02}/png/{}.png'.
            format(
                date.year,
                date.month,
                date.day,
                img['image']
            )
        )
    return epic_urls


def main():
    api_key = os.getenv('NASA_API_KEY')
    epic_urls = get_urls_from_epic(
        api_key=api_key
    )
    download_images(epic_urls, os.getenv('CATALOG'), api_key)


if __name__ == '__main__':
    load_dotenv()
    main()
