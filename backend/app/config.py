# Environment config and secrets

# load .env using load_dotenv()
# keeps keys and configs tidy and secure
# this is essentially code that fetches secrets from the .env file so that the secrets & variables stay secret

import os
from dotenv import load_dotenv

load_dotenv()

WIKI_API_URL = os.getenv("WIKI_API_URL")