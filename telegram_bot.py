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


def main():
    token = os.getenv('TELEGRAM_TOKEN')
    id_group = os.getenv('TELEGRAM_GROUP_ID')

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "message",
        nargs='?',
        default='Test message',
        help="text massege for telegram group"
    )
    args = parser.parse_args()

    send_text_message_to_group(token, id_group, args.message)


if __name__ == '__main__':
    main()
