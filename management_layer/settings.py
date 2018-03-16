import logging
import os


CACHE_TIME = 5 * 60

# Authentication middleware related settings
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_AUDIENCE = os.getenv("JWT_AUDIENCE")

# Warning: Never set this to true on a production system as it
# bypasses token authentication.
INSECURE = os.getenv("INSECURE", "False").lower() == "true"

# The port to listen on
PORT = os.getenv("SERVER_PORT", 8000)
WITH_UI = os.getenv("WITH_UI", "False").lower() == "true"

# API locations
ACCESS_CONTROL_API = os.getenv("ACCESS_CONTROL_API")
AUTHENTICATION_SERVICE_API = os.getenv("AUTHENTICATION_SERVICE_API")
USER_DATA_STORE_API = os.getenv("USER_DATA_STORE_API")

# API KEYS
ACCESS_CONTROL_API_KEY = os.environ["ACCESS_CONTROL_API_KEY"]
AUTHENTICATION_SERVICE_API_KEY = os.environ["AUTHENTICATION_SERVICE_API_KEY"]
USER_DATA_STORE_API_KEY = os.environ["USER_DATA_STORE_API_KEY"]

LOG_LEVEL = logging.DEBUG
