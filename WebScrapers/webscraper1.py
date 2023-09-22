import requests
from bs4 import BeautifulSoup

url = 'https://12695.portal.athenahealth.com'
response = requests.get(url)
print(response)