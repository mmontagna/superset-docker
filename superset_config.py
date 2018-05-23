import os
import json

SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY', '')
MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
CACHE_CONFIG = dict([(x, os.environ[x]) for x in os.environ.keys() if x.startswith('CACHE_')])

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', '')

ROW_LIMIT = int(os.getenv('ROW_LIMIT', 50000))
VIZ_ROW_LIMIT = int(os.getenv('VIZ_ROW_LIMIT', 50000))



SUPERSET_WEBSERVER_ADDRESS = os.getenv('SUPERSET_WEBSERVER_ADDRESS', '0.0.0.0')
SUPERSET_WEBSERVER_PORT = int(os.getenv('SUPERSET_WEBSERVER_PORT', 8088))
SUPERSET_WEBSERVER_TIMEOUT = int(os.getenv('SUPERSET_WEBSERVER_TIMEOUT', 80))

SQLALCHEMY_TRACK_MODIFICATIONS = False

ENABLE_CORS = 'ENABLE_CORS' in os.environ
CORS_OPTIONS = json.loads(os.environ.get('CORS_OPTIONS', '{}'))

LOG_FORMAT = os.environ.get('LOG_FORMAT', '%(asctime)s:%(levelname)s:%(name)s:%(message)s')
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

