import requests
from urllib.parse import urlsplit
import os
import telegram


def get_extension(file: str) -> str:
    __, path = os.path.split(file)
    __, extension = os.path.splitext(path)
    return extension


def get_file_name(url: str) -> str:
    __, file_name = os.path.split(urlsplit(url).path)
    return file_name


def get_images(catalog: str) -> list:
    images = []
    for adr, dir, file in os.walk(catalog):
        for img in file:
            images.append(os.path.join(adr, img))
    return images


def publish_photo_to_telegram(token: str, group_id: str, file: str):
    bot = telegram.Bot(token=token)
    with open(file, 'rb') as photo:
        bot.send_photo(
            chat_id=group_id,
            photo=photo
        )


def download_images(urls: list, path: str, api_key=None) -> None:
    params = {}
    if api_key:
        params['api_key'] = api_key

    for url in urls:
        pic = requests.get(url, params=params)
        pic.raise_for_status()

        os.makedirs(path, exist_ok=True)

        file_name = get_file_name(url)

        with open(f'{path}/{file_name}', 'wb') as file:
            file.write(pic.content)
