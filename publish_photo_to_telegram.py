import os
import argparse
from random import shuffle
from service_func import get_images, publish_photo_to_telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    group_id = os.getenv('TELEGRAM_GROUP_ID')
    catalog = os.getenv('CATALOG')

    parser = argparse.ArgumentParser(
        description='Script for posting photos to a telegram group'
    )
    parser.add_argument(
        "file_name",
        nargs='?',
        default='',
        help="Publish specific file to telegram. If not specified, \
a random photo from the catalog will be published"
    )
    args = parser.parse_args()

    if args.file_name:
        file_name = args.file_name
    else:
        images = get_images(catalog)
        shuffle(images)
        file_name = images[0]

    publish_photo_to_telegram(token, group_id, file_name)


if __name__ == '__main__':
    main()
