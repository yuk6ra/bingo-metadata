import random
import json
import string


MAIN_PATH = f'./'
DATA_FOLDER_NAME = "metadata"
SAVE_DATA_PATH = f'{MAIN_PATH}/{DATA_FOLDER_NAME}'

SUPPLY = 100
IMAGE_CID = "QmXvb8iSGeXUVSSxQaBDmwwT2EwVtDTjWiMQWPNXKjKKUj"
ANIMATION_CID = "QmQyUkK3K7rqt5VrdGeQmfgszFX5bfyo83pymeSi2JnKHa"

def main():
    # supply = int(input("supply:"))
    # image = input("imageURI:")
    # animation_url = input("animationURI:")
    supply = SUPPLY
    image = IMAGE_CID
    animation_url = ANIMATION_CID
    for token_id in range(1, supply+1):
        metadata = create_metadata(token_id, image, animation_url)
        output(metadata, token_id)

def output(data, token_id):
    template = open('template_metadata.json', 'r')

    reader = string.Template(template.read())
    json = reader.safe_substitute(data)

    with open(f'{SAVE_DATA_PATH}/{token_id}', mode='w') as file:
        file.write(json)

def create_metadata(token_id, image, animation_url):

    data = {
        "token_id": token_id,
        # "image": f"ipfs://{image}/",
        "image": f"https://bingo.yuk6ra.com/assets/bingo.png",
        # "animation_url": f"ipfs://{animation_url}/{token_id}.html",
        "animation_url": f"https://bingo.yuk6ra.com/bingo/{token_id}.html",
    }

    return data


if __name__ == '__main__':
    main()

    