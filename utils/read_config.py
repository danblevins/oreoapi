import json

def read_config():
    with open('config.json') as config:
        config = json.load(config)

    return config