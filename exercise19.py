from bs4 import BeautifulSoup
import requests
url='https://www.carwale.com/news/hyundai-bayon-spotted-beside-maruti-victoris/'

base=requests.get(url)
print(base.status_code)

soup=BeautifulSoup(base.content,"html.parser")
for p in soup.find_all('p'):
    text=p.get_text('',strip=True)
    if 'Hyundai Bayon'in text:
        print(text)
    
