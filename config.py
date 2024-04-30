import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

BASE_URL = config['URLs']['BASE_URL']
AUTHORIZATION_PASSWORD_URL = config['URLs']['AUTHORIZATION_PASSWORD_URL']
