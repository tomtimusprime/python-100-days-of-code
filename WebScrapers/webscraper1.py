import requests
from bs4 import BeautifulSoup

def get_clinic_name(clinic_id):
    url = f'https://{clinic_id}.portal.athenahealth.com'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    clinic_name = soup.find_all('h1')[-1].text.strip()
    return clinic_name
print(get_clinic_name(12695)) #the strip function takes out all the spaces and tabs.
