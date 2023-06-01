#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import string

result = requests.get('https://www.taiwan.net.tw/m1.aspx?sNo=0001016&id=290')
print(result)
result.encoding = 'UTF-8'
soup = BeautifulSoup(result.text, "html.parser")

#print(soup)

soup.find_all('div class="noJsViewPic"')
print(soup.find_all('div class="noJsViewPic"'))


def main():
    resp = requests.get('https://www.taiwan.net.tw/m1.aspx?sNo=0001016&id=290')
    soup = BeautifulSoup(resp.text, 'html.parser')
   
    #方法一
    # 找出所有 .png 結尾的圖片
    imgs = soup.find_all('img')
   
    
    for img in imgs:
        if 'src' in img.attrs:
            if img['src'].endswith('.jpg'):
                print(img['src'])
