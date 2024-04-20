import os
import requests
import json

headers = {
  'X-CMC_PRO_API_KEY' : os.getenv('X-CMC_PRO_API_KEY')

}

print(headers)