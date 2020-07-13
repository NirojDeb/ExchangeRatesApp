from .config_error import ConfigError
from currency_converter.core import DbClient

def get_config():
    config=None
    with DbClient('exchange_rates',config) as db:
        config=db.find_one()

    if config is None:
        raise ConfigError("CONFIG ERROR")
    return config    