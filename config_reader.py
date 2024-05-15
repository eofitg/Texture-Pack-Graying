import yaml


with open('./config.yml', 'r',encoding="utf-8") as f:
    config = yaml.safe_load(f)


def get(key_list):
    value = config
    keys = key_list.split('.')
    for key in keys:
        value = value[key]
    return value
