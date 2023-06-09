#select()方法取得博客來旅遊書書名與價格

import requests
from bs4 import BeautifulSoup
#博客來寵物旅遊書
url='https://www.books.com.tw/web/sys_bbotm/books/110101/?loc=P_0001_3_001' 
response=requests.get(url)   #使用requests的get()方法傳回可擷取網頁資訊response物件
response.encoding = 'utf-8'  #設定編碼模式避免亂碼
#使用BeautifulSoup()函式取得解析網頁的BeautifulSoup物件bs
bs=BeautifulSoup(response.text,"html.parser")
listName=bs.select('div.item>div.msg>h4>a')   #根據路徑擷取<a>標籤，並指定給listName串列
listPrice=bs.select('li.set2')                #取得套用set2類別的<li>標籤，並指定給listPrice串列
for i in range(0, len(listName)):             #使用迴圈逐一印出書名與書價
    print("%s\n  %s\n"%(listName[i].text, listPrice[i].text))     
