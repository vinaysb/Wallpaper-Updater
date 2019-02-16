import toml
import datetime


def config_saver(obj, file_name):
    with open(file_name, 'w+') as f:
        f.write(toml.dumps(obj))


def config_loader(file_name):
    try:
        return toml.load(file_name)
    except FileNotFoundError:
        return ({'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'currentimg': 6})
