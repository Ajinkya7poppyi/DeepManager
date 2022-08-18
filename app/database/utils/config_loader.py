import json
import os


def parse_config(filename):
    with open(filename) as f:
        return json.load(f)


def get_env():
    return os.getenv("ENV_TYPE")


def env_config(ENV_TYPE, config, app_config):
    return {
        **config["GLOBAL"],
        **config[ENV_TYPE],
        **app_config["GLOBAL"],
        **app_config[ENV_TYPE],
    }


def load_config(
    secret_file="app/config/app_config.json",
    app_config_file="app/config/app_config.json",
    full=False,
):
    config = parse_config(filename=secret_file)
    app_config = parse_config(filename=app_config_file)
    if full:
        return config, app_config
    env_type = get_env()
    try:
        c = env_config(ENV_TYPE=env_type, config=config, app_config=app_config)
    except:
        c = env_config(ENV_TYPE="DEV", config=config, app_config=app_config)
    finally:
        return c


title = "Test"
try:
    ENV_TYPE = get_env()
except TypeError:
    ENV_TYPE = "DEV"

try:
    config = load_config()
except FileNotFoundError:
    global secret_config, app_config
    try:
        secret_config
    except NameError:
        secret_config = "../../config.json"
    try:
        app_config
    except NameError:
        app_config = "../app_config.json"
    config = load_config(secret_file=secret_config, app_config_file=app_config)

PORT = config["port"]
DATABASE_NAME = config["Database"]["db_name"]
DATABASE_URL = config["Database"]["db_url"]
DATABASE_PORT = config["Database"]["db_port"]
DATABASE_USERNAME = config["Database"]["db_username"]
DATABASE_PASSWORD = config["Database"]["db_password"]
