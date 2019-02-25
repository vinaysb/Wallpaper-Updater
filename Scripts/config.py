import toml


def config_saver(obj, file_name):
    with open(file_name, "w+") as f:
        f.write(toml.dumps(obj))


def config_loader(file_name):
    try:
        return toml.load(file_name)
    except FileNotFoundError:
        return ({"date": 0, "currentimg": 6, "subreddit_name": "wallpapers"})
