import random
import json
import string

MAIN_PATH = f'..'
DATA_FOLDER_NAME = "revealed_metadata"
SAVE_DATA_PATH = f'{MAIN_PATH}/{DATA_FOLDER_NAME}'

SUPPLY = 100
IMAGE_URI = "https://bingo.yuk6ra.com/assets/revealed.png"

def main():
    # supply = int(input("supply:"))
    # image = input("imageURI:")
    # animation_url = input("animationURI:")
    supply = SUPPLY
    image = IMAGE_URI
    for token_id in range(1, supply + 1):
        metadata = create_metadata(token_id, image)
        output(metadata, token_id)


def output(data, token_id):
    template = open('../templates/template_revealed.json', 'r')

    reader = string.Template(template.read())
    json = reader.safe_substitute(data)

    with open(f'{SAVE_DATA_PATH}/{token_id}', mode='w') as file:
        file.write(json)


def create_metadata(token_id, image):
    data = {
        "token_id": token_id,
        "description": "TEST",
        "image": image,
    }

    return data


if __name__ == '__main__':
    main()

