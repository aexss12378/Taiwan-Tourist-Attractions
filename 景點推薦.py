#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import string

result = requests.get('https://www.taiwan.net.tw/')
print(result)
result.encoding = 'UTF-8'
soup = BeautifulSoup(result.text, "html.parser")

#print(soup)

soup.find('figcaption')
print(soup.find('figcaption'))
for i in range(0, len(listName)):             
    print("%s\n  %s\n"%(listName[i].text, listPrice[i].text))  
