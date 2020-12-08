import logging
from os import getenv

logger = logging


class Config(object):
    env = getenv('ENV', 'product')  # use test for test, devlop for devlop
    secret_key = getenv('SECRET_KEY', b'secretkey')
