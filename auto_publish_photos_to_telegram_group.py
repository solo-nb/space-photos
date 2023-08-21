from os import getenv, path
from random import shuffle
from service_func import publish_photo_to_telegram, get_extension, get_images
from time import sleep
from dotenv import load_dotenv


MAX_ALLOWED_IMG_SIZE = 15000000


def auto_publish_photos_to_telegram(token: str,
                                    group_id: str,
                                    catalog: str,
                                    pause_time: int):
    images = get_images(catalog)

    while True:
        for img in images:
            if path.getsize(img) > MAX_ALLOWED_IMG_SIZE:
                continue

            extension = get_extension(img)
            if extension not in ['.png', '.jpg', '.gif']:
                continue

            publish_photo_to_telegram(token, group_id, img)

            sleep(pause_time * 60 * 60)

        shuffle(images)


def main():
    load_dotenv()
    token = getenv('TELEGRAM_TOKEN')
    group_id = getenv('TELEGRAM_GROUP_ID')
    catalog = getenv('CATALOG')
    pause_time = int(getenv('PAUSE_TIME'))

    auto_publish_photos_to_telegram(token, group_id, catalog, pause_time)


if __name__ == '__main__':
    main()
