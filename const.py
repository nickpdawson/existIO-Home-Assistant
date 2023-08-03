from datetime import timedelta

NAME = "Exist.io"
DOMAIN = "exist_io"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "1.0.0"
ATTRIBUTION = "Data provided by http://exist.io"
ISSUE_URL = "https://github.com/alandtse/exist/issues"
ICON = "mdi:format-quote-close"
SENSOR = "sensor"
PLATFORMS = [SENSOR]
CONF_ENABLED = "enabled"
CONF_USERNAME = "username"
CONF_TOKEN = "token"
DEFAULT_NAME = DOMAIN
API_ENDPOINT = 'https://exist.io/api/2/attributes/with-values/'
TIMEOUT = 10
COORDINATOR = "coordinator"
API = "api"
API_TIMEOUT = 60
SENSOR = "sensor"
SENSOR_NAME = "Exist.io"
ATTR_DATE = "date"
ATTR_NAME = "name"
ATTR_ACTIVE = "active"
ATTR_SERVICE = "service"
ATTR_VALUES = "values"
ATTR_VALUE = "value"
ATTR_LABEL = "label"
ATTR_GROUP = "group"
ATTR_PRIORITY = "priority"
ATTR_VALUE_TYPE = "value_type"
ATTR_VALUE_TYPE_DESCRIPTION = "value_type_description"
SCAN_INTERVAL = timedelta(minutes=15)
