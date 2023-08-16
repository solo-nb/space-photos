from os import getenv, walk, path
from random import shuffle
from service_func import publish_photo_to_telegram, get_extension
from time import sleep


def get_images(catalog: str) -> list:
    images = []
    for adr, dir, file in walk(catalog):
        for img in file:
            images.append(path.join(adr, img))
    return images


def main():
    token = getenv('TELEGRAM_TOKEN')
    id_group = getenv('TELEGRAM_GROUP_ID')
    catalog = getenv('CATALOG')
    pause_time = int(getenv('PAUSE_TIME'))
    images = get_images(catalog)

    while True:
        for index in range(len(images)):
            img = images[index]
            if path.getsize(img) > 15000000:
                continue

            extension = get_extension(img)
            if not (extension == '.png'
                    or extension == '.jpg'
                    or extension == '.gif'):
                continue

            publish_photo_to_telegram(token, id_group, img)

            if index == len(images) - 1:
                index = 0
                shuffle(images)
            sleep(pause_time * 60 * 60)


if __name__ == '__main__':
    main()
