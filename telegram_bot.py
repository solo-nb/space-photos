import telegram
import os
import argparse
from dotenv import load_dotenv
load_dotenv()


def send_text_message_to_group(token: str, id_group: str, message: str):
    telegram.Bot(token=token).send_message(
        chat_id=id_group,
        text=message
    )


def send_photo_to_group(token: str, id_group, file):
    telegram.Bot(token=token).send_photo(
        chat_id=id_group,
        photo=open(file, 'rb')
    )


def main():
    token = os.getenv('TELEGRAM_TOKEN')
    id_group = os.getenv('TELEGRAM_GROUP_ID')

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m',
        '--message',
        default=None,
        help='text massege for sending to telegram group'
    )
    parser.add_argument(
        '-p',
        '--photo',
        default=None,
        help='file name for sending to telegram group'
    )
    args = parser.parse_args()

    if args.message:
        send_text_message_to_group(token, id_group, args.message)

    if args.photo:
        send_photo_to_group(token, id_group, args.photo)


if __name__ == '__main__':
    main()
