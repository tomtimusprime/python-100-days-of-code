import requests
from bs4 import BeautifulSoup

url = 'https://12695.portal.athenahealth.com'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
print(soup.title.text.strip()) #the strip function takes out all the spaces and tabs.
print("web scraper.")
print("web scraper.")
print("Web scraper.")