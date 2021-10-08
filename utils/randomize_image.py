import os
import random
from utils.read_config import read_config

config = read_config()

def randomize_image():
    images = [img for img in os.listdir(config["images"])]
    image = random.choice(images)

    return image