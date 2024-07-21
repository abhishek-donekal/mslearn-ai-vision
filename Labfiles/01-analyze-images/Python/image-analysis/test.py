import os
import requests
from dotenv import load_dotenv

load_dotenv()
ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
ai_key = os.getenv('AI_SERVICE_KEY')

headers = {
    'Ocp-Apim-Subscription-Key': ai_key
}

try:
    response = requests.get(ai_endpoint, headers=headers)
    print(response.status_code)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(e)
