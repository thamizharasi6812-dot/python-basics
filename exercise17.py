from bs4 import BeautifulSoup
import requests
url="https://www.carwale.com/"
 
base=requests.get(url)
print(base.status_code)
 
soup=BeautifulSoup(base.content,"html.parser")
element=soup.find("div",class_="dVKXT2 o-t pq6DJv o-ci" )
name=element.find_all("div",class_="o-o aXlX4B o-hl o-iT o-jq o-j3 o-jj o-bM o-cZ o-ci o-dv o-cA o-dN o-c4 o-dh o-jH")
price=element.find_all("div",class_="o-cA o-dN o-c4 o-dh o-aE o-f")

for i in range(len(price)):
 print(name[i].text,price[i].text)


from bs4 import BeautifulSoup
import requests
url="https://www.carwale.com/"
 
base=requests.get(url)
print(base.status_code)
 
soup=BeautifulSoup(base.content,"html.parser")
element=soup.find("div", class_="dVKXT2 o-t pq6DJv o-bO o-ck " )
name=element.find_all("div",class_="o-o aXlX4B o-hl o-iT o-jq o-j3 o-jj o-bM o-cZ o-ci o-dv o-cA o-dN o-c4 o-dh o-jH")
price=element.find_all("div",class_="o-cA o-dN o-c4 o-dh o-aE o-f")
for i in range(len(price)):
 print(name[i].text,price[i].text)

from bs4 import BeautifulSoup
import requests
url='https://webscraper.io/test-sites/e-commerce/static'

base=requests.get(url)
print(base.status_code)

soup=BeautifulSoup(base.content,'html.parser')
total=soup.find('div',class_="wrapper")
name=total.find('div',class_="caption")
price=total.find_all('span',iteamprop_='price')
description=total.find_all('p',class_="description card-text")
memory=total.find_all('div',class_="swatches")


for i in range (len(price)):
 print(price[i].text,description[i].text,memory[i].text)