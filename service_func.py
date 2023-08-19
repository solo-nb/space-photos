import requests
from urllib.parse import urlsplit
import os
import telegram
from dotenv import load_dotenv


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
    with open(file, 'rb') as photo:
        telegram.Bot(token=token).send_photo(
            chat_id=group_id,
            photo=photo
        )


def download_image(url: str, path: str, api_key: str) -> None:
    params = {}
    if api_key:
        params['api_key'] = api_key

    pic = requests.get(url, params=params)
    pic.raise_for_status()

    if not os.path.exists(path):
        os.makedirs(path)

    file_name = get_file_name(url)

    with open(f'{path}/{file_name}', 'wb') as file:
        file.write(pic.content)


def download_images(urls: list, path: str, api_key=None) -> None:
    for url in urls:
        download_image(url, path, api_key)


if __name__ == '__main__':
    load_dotenv()
