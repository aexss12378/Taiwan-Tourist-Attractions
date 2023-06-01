#擷取網頁圖片
#pip3 install requests

import requests
img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
response= requests.get(img_url) 
f=open('D:\\拍森\\AEL022200.jpg','wb') #指定存放路徑
# 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
f.write(response.content)  			
print('下載完畢')
f.close()
