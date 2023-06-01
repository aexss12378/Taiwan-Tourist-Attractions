#主題：台灣觀光局網站
#Subject: Sightseeing Planning
#內容：人數控管、天氣、預算、景點類型、中英文、推薦行程、景點介紹、日曆看
#開放時間、估價花費
#Content: Human CNC control, weather, budget, attraction type, Chinese and English, recommended itinerary, attraction introduction, calendar to see opening time, estimated cost
#海邊戲水、宗教文化、藝術空間、觀光夜市、森林洞穴
#Seaside playing, religious culture, art space, tourist night market, forest cave

import calendar 
Estimated_amount=[]


print('台灣旅遊景點簡介\n')


#中英文
print('選擇語言 Choose a language : 1=中文 、 2=English')
language = int(input())


if language ==1:
  print('請輸入預計旅遊日期，來查詢景點是否開放')
  y=int(input("年份："))
  m=int(input("月份："))
  d=int(input("日期："))
  Week = ("星期一","星期二","星期三","星期四","星期五","星期六","星期日")
  print(y,'/',m,'/',d,'/',Week[calendar.weekday(y, m, d)],'\n')

else:
  print("please enter a date mm/dd/yyyy: ") 
  m=int(input("month: "))
  d=int(input("day: "))
  y=int(input("year: "))
  Week = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
  print(y,'/',m,'/',d,'/',Week[calendar.weekday(y, m, d)],'\n')



###################################################################################



def Taichung_National_Opera_C():
  print('景點名稱:臺中國家歌劇院\n景點類型:藝術空間\n費用:300\n地址:\n臺中市西屯區惠來路二段101號\n營業時間:\n星期日: 11:30 – 21:00\n星期一: 休息\n星期二: 11:30 – 21:00\n星期三: 11:30 – 21:00\n星期四: 11:30 – 21:00\n星期五: 11:30 – 22:00\n星期六: 11:30 – 22:00\n控管人數:無\n景點介紹:\n位於臺中市西屯區七期重劃區，是一大型公有展演空間，由曾獲普立茲克獎的日本建築師伊東豊雄設計。臺中國家歌劇院得天獨厚，在這完美建築之內，有三座專業劇場以及一個多功能空間「角落沙龍」。\n從設計之初到建築完工，歌劇院歷經了時光的淬鍊與嚴峻的考驗。在競圖階段，伊東豊雄採用前衛的設計觀點、挑戰既有的思考模式，預先構思建築的輪廓，再依表演特性將舞台置入曲牆中。第二階段則著重空間效益，檢視設計結構的可行方案，並創新連接大劇院與中劇院的前廳。最後根據歌劇院內部視覺、聽覺等感受，將動線進行微調，回歸到「人」與空間的互動，強調迴盪在「美聲涵洞」（Sound Cave）的藝術能量。表演藝術所要呈現的歡笑、憂傷與感動，都因此獲得渲染與加乘的效果。\n')
  Estimated_amount.append(300)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022200.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()

def Taichung_National_Opera_E():
  print('Attraction Name: Taichung National Opera\nAttraction Type: Art Space\nCost: 300\nAddress:\nNo.101, Section 2, Huilai Road, Xitun District, Taichung City\nBusiness Hours:\nSunday: 11 :30 – 21:00\nMonday: closed\nTuesday: 11:30 – 21:00\nWednesday: 11:30 – 21:00\nThursday: 11:30 – 21:00\nFriday: 11 :30 – 22:00\nSaturday: 11:30 – 22:00\nNumber of people controlled: None\nIntroduction of attractions:\nLocated in the re-zoning area of ​​the seventh phase of Xitun District, Taichung City, it is a large public performance space. Designed by the Pritzker Prize-winning Japanese architect Toyohio Ito. Taichung National Opera is uniquely endowed by nature. Within this perfect building, there are three professional theaters and a multifunctional space "Corner Salon."\nFrom the beginning of the design to Upon completion of the building, the opera house has withstood the hardening of time and the severe test. In the stage of competition, Toyohio Ito adopted avant-garde design viewpoints and challenged existing thinking modes, pre-conceived the outline of the building, and then placed the stage in accordance with the performance characteristics. In the curved wall. The second stage focuses on space efficiency, examines the feasible schemes of the design structure, and innovates the front hall connecting the Grand Theater and the Central Theater. Finally, according to the internal visual and auditory feelings of the Opera House, the movement lines are fine-tuned and returned to The interaction between "people" and space emphasizes the artistic energy reverberating in the "Sound Cave." The laughter, sadness, and emotion that the performing arts want to present are all rendered and multiplied.\n')
  Estimated_amount.append(300)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022200.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  ###################
  from requests_html import HTMLSession
  s = HTMLSession()
  query = 'Xitun+District+Taichung+City'
  url = f'https://www.google.com/search?q=weather+{query}'
  r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
  temp = (r.html.find('span#wob_tm', first=True).text)
  unit = (r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text)
  descrip = (r.html.find('div.VQF4g', first=True).find('span#wob_dc',first=True).text)
  print("The current weather at Taichung National Opera, located in Xitun District, Taichung City is "+str(temp)+str(unit)+str(descrip))

def Caogong_Taoist_Temple_C():
  print('景點名稱:曹公廟\n景點類型:宗教寺廟\n費用:免費\n地址:高雄市鳳山區曹公路25-3號\n營業時間:7：30 ~ 19：00\n控管人數:無\n景點介紹:\n相傳當時的鳳山知縣曹謹利用開鑿水圳的方法，引取高屏溪水讓鳳山縣內農田得以種植作物，後代子孫為了感念他的傳付出，特立「曹公祠」祭祀，民國81年間，相傳玉皇大帝降旨將曹公祠升格為曹公廟，自此信眾改奉曹公神像，並正式改稱為「曹公廟」。\n')
  Estimated_amount.append(100)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022201.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()

def Caogong_Taoist_Temple_E():
  print('Attraction Name: Caogong Temple\nAttraction type: religious temple\nCost: Free\nAddress: No. 25-3, Cao Road, Fengshan District, Kaohsiung City\nBusiness hours: 7:30 ~ 19:00\nNumber of people under control: None\nAttractions:\nAccording to legend, Cao Jin, the magistrate of Fengshan at that time, used the method of digging a canal to attract the Gaoping stream to grow crops in the farmland in Fengshan County. In order to thank him for his dedication, future generations set up a special "Cao Gong Temple" memorial site. In 1981, According to legend, the Jade Emperor decree upgraded Cao Gong memorial site to Cao Gong Temple. Since then, believers have changed to the statue of Cao Gong and officially renamed it "Cao Gong Temple."\n')
  Estimated_amount.append(100)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022201.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################
  from requests_html import HTMLSession
  s = HTMLSession()
  query = 'Fengshan+District+Kaohsiung+City'
  url = f'https://www.google.com/search?q=weather+{query}'
  r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
  temp = (r.html.find('span#wob_tm', first=True).text)
  unit = (r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text)
  descrip = (r.html.find('div.VQF4g', first=True).find('span#wob_dc',first=True).text)
  print("The current weather at Caogong Taoist Temple, located in Fengshan District, Kaohsiung City is "+str(temp)+str(unit)+str(descrip))

def Liugui_Giant_Buddha_C():
  print('景點名稱:彩虹山大佛/六龜大佛\n景點類型:特色文化/宗教寺廟費用(香油錢):300\n地址:高雄市六龜區新發里新開路27-1號\n營業時間:8:00 ~ 17:00 \n控管人數:無\n景點介紹:\n六龜大佛共使用了167噸銅雕鑄造而成，採閉眼坐像，高20公尺(約七層樓)；莊嚴慈目聳立於山林間，居高臨下俯瞰眾生，充滿寧靜祥和的氣度。前方為朝山如意大梯，兩道階梯中央有著刻滿九龍石雕的御路，兩旁石柱上還有龍形石雕和雕刻精細的石壁畫；佛前還有座參拜平台，放置大型的銅香爐和銅祭台，型態傳統華麗不比一般；循線登上階梯攀爬至頂即可抵達大佛處。\n')
  Estimated_amount.append(0)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022202.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################

def Liugui_Giant_Buddha_E():
  print('Attraction Name: Rainbow Mountain Giant Buddha / Liugui Giant Buddha\nAttraction type: characteristic culture/religious temple\nCost: 300\nAddress: No. 27-1, Xinkai Road, Xinfali, Liugui District, Kaohsiung City\nBusiness hours: 8:00 ~ 17:00\nNumber of people under control: None\nAttractions:\nThe Liugui Giant Buddha was cast from a total of 167 tons of bronze sculptures. It is a seated statue with closed eyes. It is 20 meters high (about seven stories). The majestic and benevolent eyes tower over the mountains and forests. There is a large ladder towards the mountain in front. There is an imperial road engraved with nine dragon stone carvings in the center of the two stairs. On both sides of the stone pillars there are dragon-shaped stone carvings and finely carved stone murals. There is also a worship platform in front of the Buddha, where a large copper incense burner and a copper sacrifice are placed. The platform is traditionally gorgeous and gorgeous; follow the line up the stairs and climb to the top to reach the Big Buddha.\n')
  Estimated_amount.append(300)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022202.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################
  from requests_html import HTMLSession
  s = HTMLSession()
  query = 'Liugui+District+Kaohsiung+City'
  url = f'https://www.google.com/search?q=weather+{query}'
  r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
  temp = (r.html.find('span#wob_tm', first=True).text)
  unit = (r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text)
  descrip = (r.html.find('div.VQF4g', first=True).find('span#wob_dc',first=True).text)
  print("The current weather at Liugui Giant Buddha, located in Liugui District, Kaohsiung City is "+str(temp)+str(unit)+str(descrip))
  
def Shiti_Port_C():
  print('關於石梯港\n石梯港(石梯漁港)位於花蓮縣豐濱鄉，石梯坪的西北邊，是台灣地區的賞鯨發源地，於1957年至1963年間由花蓮港務局闙建而成，屬於多功能休閒漁港，更入圍2011年十大魅力漁港票選資格。石梯漁港內以及長達800公尺的防波堤上點綴不少立體造景的鯨豚圖雕，更蒐集了漁村風光、漁民作業以及阿美族文物介紹等。\n地址：\n花蓮縣豐濱鄉港口村石梯灣96號\n景觀特色：\n台灣賞鯨發源地，鯨豚發現率高達百分之九十五，為全台之冠。\n建議停留時間：\n60分鐘\n營業(開放)時間：\n石梯港／洽詢電話:03-8781233\n服務設施：\n東管處石梯坪遊客服務中心\n地址：花蓮縣豐濱鄉港口村石梯坪52號\n電話：03-8781452\n提供活動：\n每年約4月至10月賞鯨季節，當地賞鯨船業者推出搭船賞鯨活動。\n')
  Estimated_amount.append(500)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022203.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################

def Shiti_Port_E():
  print('About Shiti Port\nShiti Port (Shiti Fishing Port) is located in Fengbin Township, Hualien County, to the northwest of Shitiping. It is the birthplace of whale watching in Taiwan. It was built by the Hualien Port Authority from 1957 to 1963. It is a multifunctional recreational fishing port. It was also shortlisted for the vote for the top ten charming fishing ports in 2011. In the Shiti Fishing Port and on the 800-meter-long breakwater, there are many three-dimensional sculptures of whales and dolphins, as well as the scenery of the fishing village, the work of the fishermen, and the introduction of Amis cultural relics.\naddress:\nNo. 96, Shitiwan, Gangkou Village, Fengbin Township, Hualien County\nLandscape features:\nIn the birthplace of whale watching in Taiwan, the discovery rate of whales and dolphins is as high as 95%, which is the highest in Taiwan.\nSuggested stay time:\n60 minutes\nBusiness (opening) hours:\nShiti Port / Inquiries: 03-8781233\nService Facilities:\nShitiping Tourist Service Center, East Administration Office\nAddress: 52 Shitiping, Gangkou Village, Fengbin Township, Hualien County\nPhone: 03-8781452\nProvide activities:\nDuring the whale watching season from April to October every year, local whale watching boat operators launch whale watching activities on boats.\n')
  Estimated_amount.append(500)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022203.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################
  from requests_html import HTMLSession
  s = HTMLSession()
  query = 'Fengbin+Township+Hualien+County'
  url = f'https://www.google.com/search?q=weather+{query}'
  r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
  temp = (r.html.find('span#wob_tm', first=True).text)
  unit = (r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text)
  descrip = (r.html.find('div.VQF4g', first=True).find('span#wob_dc',first=True).text)
  print('The current weather at Shiti Port, located in Fengbin Township, Hualien County, Taiwan is '+str(temp)+str(unit)+str(descrip))

def Green_Island_Lighthouse_C():
  print('西元1939年建造的綠島燈塔，位在台東綠島鄉的西北海岸高地，塔身為圓形鋼筋混泥土結構。燈塔矗立於機場跑道北端的海岬上，在塔頂可俯瞰全島，潔白的塔身與碧海藍天輝映，成為遊客留影的最佳背景；當夜晚降臨時，點亮光芒的燈塔，不時劃過天際，與滿天星斗相襯，美麗的景致也是攝影師拍攝銀河星空的好地方。\n電話 089-672540\n開放時間 【綠島燈塔開放時間】\n4月-10月：9:00-18:00\n11月-3月：9:00-17:00\n每週一(內部整修及維護)不開放。\n門票資訊 免費\n')
  Estimated_amount.append(0)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022204.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################

def Green_Island_Lighthouse_E():
  print("The Green Island Lighthouse, built in 1939, is located on the northwest coast of Taitung's Ludao Township.The tower is a circular reinforced concrete structure.The lighthouse stands on the promontory at the northern end of the airport runway. From the top of the tower, you can overlook the whole island. The white tower body and the blue sea and blue sky are the best background for tourists to take photos. When the night falls, the lighted up lighthouse will flash across the sky from time to time. In contrast to the starry sky, the beautiful scenery is also a good place for photographers to take pictures of the Milky Way and stars.\nLocation: 95141, Taitung County, Lvdao Township, Taiwan,燈塔1號\nPhone 089-672540\nOpening Hours [Opening Hours of Green Island Lighthouse]\nApril-October: 9:00-18:00\nNovember to March: 9:00-17:00\nIt is closed every Monday (internal renovation and maintenance).\nTicket Information Free\n")
  Estimated_amount.append(0)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022204.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################
  from requests_html import HTMLSession
  s = HTMLSession()
  query = 'Taitung+County+Lvdao+Township+Taiwan'
  url = f'https://www.google.com/search?q=weather+{query}'
  r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
  temp = (r.html.find('span#wob_tm', first=True).text)
  unit = (r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text)
  descrip = (r.html.find('div.VQF4g', first=True).find('span#wob_dc',first=True).text)
  print("The current weather at Green Island Lighthouse, located in Taitung County, Lvdao Township is "+str(temp)+str(unit)+str(descrip))

def Huoyan_Mountain_Trail_C():
  print('景點名稱:火炎山步道\n景點類型:森林洞穴\n費用:100\n地址:苗栗縣三義鄉\n營業時間:全天\n控管人數:無\n景點介紹:\是台灣中部少見的惡地，紅色的山壁遠看有如燎原烈火般地燃燒，因此有火炎山之稱。火炎山擁有特殊地貌與稀有動植物，已被規畫為自然保護區。\n海拔高度：223~602公尺\n里程：全程 6.4 公里\n高度落差：379公尺\n所需時間：約 3 小時\n')
  Estimated_amount.append(100)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022205.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################

def Huoyan_Mountain_Trail_E():
  print('Attraction type:Huoyan Mountain Trail\nAttraction type:forest cave\nCost: 100\nAddress:Sanyi Township, Miaoli County\nOpening hours: all day\nNumber of people under control: None\nScenic Spot Introduction: It is a rare bad land in central Taiwan. The red mountain wall burns like a prairie fire from a distance, so it is known as the Fire Mountain. Huoyan Mountain has special landforms and rare animals and plants, and has been planned as a nature reserve。\nAltitude: 223~602 meters\nMileage: 6.4 kilometers in total\nHeight drop: 379 meters\nTime required: about 3 hours\n')
  Estimated_amount.append(100)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022205.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################
  from requests_html import HTMLSession
  s = HTMLSession()
  query = 'Sanyi+Township+Miaoli+County+Taiwan'
  url = f'https://www.google.com/search?q=weather+{query}'
  r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
  temp = (r.html.find('span#wob_tm', first=True).text)
  unit = (r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text)
  descrip = (r.html.find('div.VQF4g', first=True).find('span#wob_dc',first=True).text)
  print("The current weather at Huoyan Mountain Trail, located in Sanyi Township, Miaoli County, is "+str(temp)+str(unit)+str(descrip))

def Yuanzui_Shaolaishan_National_Trail_C():
  print('景點名稱:鳶嘴稍來山國家步道\n景點類型:森林洞穴\n費用:100\n地址:臺中市和平區\n營業時間:全天\n控管人數:無\n景點介紹:\為中部地區中海拔熱門登山路線，鳶嘴山刺激具挑戰性以險峻危崖出名，而稍來山以秋天滿佈的台灣紅榨槭為名，沿途峭壁綿延、景觀秀麗。\n海拔高度：1800~2600公尺\n全程 15.2公里\n高度落差：800公尺\n所需時間：約 9 小時\n')
  Estimated_amount.append(100)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022206.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################
def Yuanzui_Shaolaishan_National_Trail_E():  
  print('Attraction type:Yuanzui Shaolaishan National Trail\nAttraction type:forest cave\nCost: 100\nAddress:Heping District, Taichung City\nOpening hours: all day\nNumber of people under control: None\nScenic Spot Introduction:It is a popular climbing route at mid-altitudes in the central region. Yuanzui Mountain is famous for its stimulating and challenging cliffs, while Shaolai Mountain is named after Taiwanese red maple in autumn. It has long cliffs and beautiful scenery along the way.\nAltitude: 1800~2600 meters\nMileage: 15.2 kilometers in total\nHeight drop: 800 meters\nTime required: about 9 hours\n')
  Estimated_amount.append(100)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022206.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################
  from requests_html import HTMLSession
  s = HTMLSession()
  query = 'Heping+District+Taichung+City'
  url = f'https://www.google.com/search?q=weather+{query}'
  r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
  temp = (r.html.find('span#wob_tm', first=True).text)
  unit = (r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text)
  descrip = (r.html.find('div.VQF4g', first=True).find('span#wob_dc',first=True).text)
  print("The current weather at Yuanzui Shaolaishan National Trail, located in Heping District, Taichung City, is "+str(temp)+str(unit)+str(descrip))

def Raohe_Street_Night_Market_E():
  print('Attraction Name: Raohe Street Night Market\nAttraction Type: Tourist Night Market\nCost: 200\nAddress: Raohe Street between and parallel to Songhe Street, Section 4 of Bade Road, Songshan District, Taipei City\nBusiness hours:\nSunday 17:00-23:00\nMonday 17:00-23:00\nTuesday 17:00-23:00\nWednesday 17:00-23:00\nThursday 17:00-23:00\nFriday 17:00-23:00\nSaturday 17:00-23:00\nAttractions:\nWhen you come to the intersection of Section 4 of Bade Road and Tayou Street, you will see the magnificent archway at the entrance and the shiny market, which is particularly conspicuous at night. When you see the owl totem symbolizing the mascot of the night market, you will know that the night market is near. In front of you.\nRaohe Street Tourist Night Market is the earliest tourist night market in Taipei. It is not large in scale and has very concentrated stalls. As long as you are regular customers, you can quickly find the stalls you want to eat, which is very convenient. Raohe Street Night Market has many must-eat delicacies. The famous oyster noodles, braised large intestines are refreshing and crisp, quite tasty; the fragrant medicinal stewed pork ribs, added with the secret recipe of traditional Chinese medicine, does not have a fishy smell, it is a holy product for dredging the bones and nourishing the body in winter; selling a variety of stewed Dongshan duck heads with good meat quality It is flexible and tastes better when iced; fresh and tender crab legs and crab meat, delicious old bean curd, and a variety of novel and delicious snacks are endless.\n')
  Estimated_amount.append(200)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022207.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################
  from requests_html import HTMLSession
  s = HTMLSession()
  query = 'Bade+Road+Songshan+District+Taipei+City'
  url = f'https://www.google.com/search?q=weather+{query}'
  r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
  temp = (r.html.find('span#wob_tm', first=True).text)
  unit = (r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text)
  descrip = (r.html.find('div.VQF4g', first=True).find('span#wob_dc',first=True).text)
  print("The current weather at Raohe Street Night Market, located in Bade Road, Songshan District, Taipei City is "+str(temp)+str(unit)+str(descrip))

def Raohe_Street_Night_Market_C():
  print('景點名稱:饒河街觀光夜市\n景點類型:觀光夜市\n預估費用:200\n地址:臺北市松山區八德路四段與松河街間且與之平行的饒河街上 \n營業時間:\n星期日 17:00 - 23:00\n星期一 17:00 - 23:00\n星期二 17:00 - 23:00\n星期三 17:00 - 23:00\n星期四 17:00 - 23:00\n星期五 17:00 - 23:00\n星期六 17:00 - 23:00\n景點介紹:\n來到八德路4段與塔悠街交叉口，看到入口處金碧輝煌的牌樓，閃閃發亮的市集，在夜間特別顯眼，再看到象徵夜市吉祥物的貓頭鷹圖騰，就知道夜市已經近在眼前。\n饒河街觀光夜市是臺北市最早的觀光夜市，規模並不大，攤位非常集中，只要是常來的熟客，很快就可以找到自己想吃的攤位，非常方便。饒河街觀光夜市有許多非吃不可的美食。有名的蚵仔麵線，滷大腸爽口夠脆、相當入味；香噴噴的藥燉排骨，加入中藥秘方，沒有腥羶味，是冬天疏通筋骨、滋補養身聖品；販賣各種滷味的東山鴨頭，肉質有彈性，冰過更好吃；鮮嫩十足的蟹腳蟹肉、好喝的古早豆花，各種新奇美味的小吃多到數不完。\n')
  Estimated_amount.append(200)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022208.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################
def Liuhe_Tourist_Night_Market_E():
  print('Attraction Name: Liuhe Tourist Night Market\nAttraction Type: Tourist Night Market\nCost: 200\nAddress: At the intersection of Liuhe 2nd Road and Zhongshan 1st Road, Xinxing District, Kaohsiung City\nBusiness hours:\nEvery night from 17:00 to 05:00 in the morning\nOpen all year round\nAttractions introduction:\nIf you have not been to Liuhe Night Market, you do not really have been to Kaohsiung. \nAs early as in the 39th year of the Republic of China (1950), many food stalls began to gather in the open space near Dagangpu, Xinxing District, Kaohsiung City. Gradually, more and more food stalls began to form. ", and then gradually expanded. Transformed into the current Liuhe Night Market. Liuhe Night Market is not far from Kaohsiung Railway Station. Walk straight along Zhongshan Road for about ten minutes and then turn right to Liuhe Road.\nDuring the day, it is a straight road. At night, it becomes a lively market with people coming and going. The "Liuhe Night Market" is famous for its diverse snacks. The most special sight is the signature steakhouses and seafood shops, large and small. There are more than 10, the main selling point is the cheap, family-style steak set menu. The two rows of stalls have everything from mountain products, seafood, specialty products to cold drinks, ice products, etc. The variety is dizzying, and the rich taste of snacks is well-known in Taiwan. Kaohsiung’s specialty papaya milk and salt-steamed prawns are delicious flavors you can’t miss. \nThe Liuhe Night Market in Kaohsiung City has successfully shaped the overall image of a world-class gourmet night market, creating new attractions for recreation and consumption. In the hardware planning part, we are committed to combining Kaohsiung’s unique port-city culture, effectively enhancing vendors and consumers’ recognition of Liuhe Night Market; in software, consolidating the centripetal and action capabilities of the overall vendors and the management committee, and actively promoting unity Uniforms and stalls have implemented the business philosophy of "improving customer satisfaction" in the service industry, creating a broad road. In recent years, the municipal government has been more active in organizing the "Traditional Market YOUNG" and "Liuhe Food Carnival" series of activities at the internationally renowned Liuhe Night Market to expand business opportunities in the business district.\n')
  Estimated_amount.append(200)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022208.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################
  from requests_html import HTMLSession
  s = HTMLSession()
  query = 'Xinxing+District+Kaohsiung+City+Taiwan'
  url = f'https://www.google.com/search?q=weather+{query}'
  r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
  temp = (r.html.find('span#wob_tm', first=True).text)
  unit = (r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text)
  descrip = (r.html.find('div.VQF4g', first=True).find('span#wob_dc',first=True).text)
  print("The current weather at Liuhe Tourist Night Market, located in Xinxing District, Kaohsiung City, Taiwan is "+str(temp)+str(unit)+str(descrip))
  
def Liuhe_Tourist_Night_Market_C():
  print('景點名稱:六合觀光夜市\n景點類型:觀光夜市\n預估費用:200\n地址:高雄市新興區六合二路與中山一路口\n營業時間:\n每晚17:00-凌晨05:00\n全年無休\n景點介紹:\n沒到過六合夜市，就不算真正去過高雄。\n早在民國39年（西元1950年），位於現在高雄市新興區大港埔附近的空地上，就開始聚集了許多小吃攤，漸漸的越來越多，久而久之便形成以小吃聞名的「大港埔夜市」，之後逐漸擴大。轉變成為現在的六合夜市。六合夜市距離高雄火車站不遠，沿著中山路直行約十餘分鐘後右轉至六合路便可到達。\n白天這裡是筆直的大馬路，到了晚上便成為人來人往的熱鬧市集，以多樣化小吃聞名的「六合夜市」，最特殊的景觀是招牌林立的牛排店及海產店，大大小小有10多家，主要賣點是平價、家庭式的牛排套餐。兩排攤位從山產、海產、特產到冷飲、冰品等應有盡有，種類之多令人目不暇給，小吃口味之豐富為全臺有名。而高雄市的特色木瓜牛奶及鹽蒸蝦更是你不可錯過的好味道。\n高雄市六合夜市成功塑造出國際級美食觀光夜市的整體形象，創造休憩、消費新景點。在硬體規劃部份致力於結合高雄特有港都文化，有效的增進攤販及消費者對六合夜市的認同感；在軟體上，凝聚整體攤販及管委會的向心力與行動力，並積極推廣統一制服與攤招，落實服務業『提昇顧客滿意度』的經營理念，開創出一條康莊大道。近年來市政府更積極在具國際知名度的六合夜市辦「傳統市集 YOUNG起來」、「六合美食嘉年華」系列活動，擴大商圈的商機。\n')
  Estimated_amount.append(200)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022210.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################
def Taitung_Tourist_Night_Market_E():
  print("Attraction Name: Taitung Tourist Night Market\nCost: 200\nAddress: Taitung City, Taitung County, in front of the Taitung Bus Station, and the righteous section on the left side of the intersection with Zhongshan Road \nBusiness hours:\nSunday: closed\nMonday: closed\nTuesday: closed\nWednesday: closed\nThursday: 17:00 – 23:00\nFriday: 17:00 – 23:00\nSaturday: 17:00 – 23:00\nAttractions introduction:\nSince the only night market in Taitung for many years is the mobile night market every Sunday evening, the location is on Siwei Road and the square in front of Ren'ai Elementary School. Many visitors to Taitung have reported that there are no other tourist activities besides bathing in Taitung at night. Taitung City is quite depressed. Since July 30, 2010, the Taitung Tourist Night Market has been in operation, allowing many tourists to have a good place to hang out at night. \nTaitung Tourist Night Market is located on Zhengqi Road. During the day, it is a fruit street selling all kinds of fruits. The store will place all kinds of fruits in front of the store for the public to choose. Many fruits that are abundant in the season are almost available here.\nOn Thursday to Saturday nights, this place is transformed into a Taitung Tourist Night Market. In addition to all kinds of snacks, there are also many amusement facilities, providing Taitung night entertainment and entertainment, and it also allows many tourists to have a good night to hang out in the evening. place. As for Sundays, the night market will be moved to Siwei Road. Those who want to try the Taitung Night Market, please don’t go to the wrong place. \n'")
  Estimated_amount.append(200)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022210.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################
  from requests_html import HTMLSession
  s = HTMLSession()
  query = 'Taitung+County+Zhongshan+Road+Taiwan'
  url = f'https://www.google.com/search?q=weather+{query}'
  r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
  temp = (r.html.find('span#wob_tm', first=True).text)
  unit = (r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text)
  descrip = (r.html.find('div.VQF4g', first=True).find('span#wob_dc',first=True).text)
  print("The current weather at Taitung Tourist Night Market, located in Taitung County, Zhongshan Road, Taiwan is "+str(temp)+str(unit)+str(descrip))

def Taitung_Tourist_Night_Market_C():
  print("景點類型:臺東觀光夜市\n預估費用:200\n地址:臺東縣臺東市鄰近臺東轉運站前方、與中山路交叉左側的正氣路段 \n營業時間:\n星期日：休息\n星期一：休息\n星期二：休息\n星期三：休息\n星期四：17:00 – 23:00\n星期五：17:00 – 23:00\n星期六：17:00 – 23:00\n景點介紹:\n由於臺東多年來唯一的夜市是每週日晚間的流動夜市，地點在四維路上、仁愛國小前廣場，許多到臺東的遊客反映，臺東到了夜間除了泡湯之外就沒有其他旅遊活動，晚間的臺東市區相當蕭條。而從2010年7月30日起，臺東觀光夜市即開始啟動經營，讓許多遊客到了晚上也多了一個可以遊逛解饞的好地方。\n臺東觀光夜市位於正氣路上，白天是販賣各式水果的水果街，店家會將各式水果放置在店前供民眾挑選，許多當季盛產的水果這邊幾乎都買得到。\n而在週四至週六夜晚，這裡搖身一變成為台東觀光夜市，除了各式小吃，也有許多遊玩的設施，提供臺東夜晚的娛樂消遣，也讓許多遊客到了晚上也多了一個可以遊逛解饞的好地方。至於週日，夜市則會移至四維路上，要來臺東夜市嘗鮮的各位，請不要跑錯地方。\n")
  Estimated_amount.append(200)
  import requests
  img_url='https://travel.taichung.gov.tw/Utility/DisplayImage?id=24379'
  response= requests.get(img_url) 
  f=open('D:\\AEL022211.jpg','wb') #指定存放路徑
  # 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
  f.write(response.content)  			
  print('下載完畢')
  f.close()
  #########################
####################################################################################


if (language ==1):
  prefer = 0
  while (prefer<6):
    print('\n景點類型:\n1=海邊戲水、2=宗教文化、3=藝術空間、4=觀光夜市、5=森林氛圍')
    prefer = int(input('請選擇喜好的景點類型(欲離開索引請按7):'))
    if prefer == 1:
      print('景點:\n1=石梯港\n2=綠島燈塔\n') 
      choose = int(input('選擇想去的景點:'))
      if choose == 1:
        Shiti_Port_C()
      else :
        Green_Island_Lighthouse_C()
    if prefer == 2:
      print('景點:\n1=曹公廟\n2=彩虹山大佛\n')
      choose = int(input('選擇想去的景點:'))
      if choose == 1:
        Caogong_Taoist_Temple_C()
      else :
        Liugui_Giant_Buddha_C()
    if prefer == 3:
      print('景點:\n1=臺中國家歌劇院\n')
      choose = int(input('選擇想去的景點:'))
      if choose == 1:
        Taichung_National_Opera_C()
    if prefer == 4:
      print('景點:\n1=饒河街觀光夜市\n2=臺東觀光夜市\n3=六合觀光夜市')
      choose = int(input('選擇想去的景點:'))
      if choose == 1:
        Raohe_Street_Night_Market_C()
      elif choose == 2:
        Taitung_Tourist_Night_Market_C()
      else :
        Liuhe_Tourist_Night_Market_C() 
    if prefer == 5:
      print('景點:\n1=火炎山步道\n2=鳶嘴稍來山國家步道\n')
      choose = int(input('選擇想去的景點:'))
      if choose == 1:
        Huoyan_Mountain_Trail_C()
      else :
        Yuanzui_Shaolaishan_National_Trail_C()
    if prefer == 6:   
      print('博客來推薦百大旅遊書') 
      import requests
      from bs4 import BeautifulSoup
      url='https://www.books.com.tw/web/sys_bbotm/books/110101/?loc=P_0001_3_001' 
      response=requests.get(url)   #使用requests的get()方法傳回可擷取網頁資訊response物件
      response.encoding = 'utf-8'  #設定編碼模式避免亂碼
      #使用BeautifulSoup()函式取得解析網頁的BeautifulSoup物件bs
      bs=BeautifulSoup(response.text,"html.parser")
      listName=bs.select('div.item>div.msg>h4>a')   #根據路徑擷取<a>標籤，並指定給listName串列
      listPrice=bs.select('li.set2')                #取得套用set2類別     的<li>標籤，並指定給listPrice串列
      for i in range(0, len(listName)):             
          print("%s\n  %s\n"%(listName[i].text, listPrice[i].text))
    if prefer == 7:
      print('預估金額:',sum(Estimated_amount))
      break
else:
  prefer = 0
  while (prefer<6):
    print('the type of attraction:\n1.sea side 2.religious 3.fine arts 4.famous night markets 5.nature trails')
    prefer = int(input('Choose the type of attraction you prefer:'))
    if prefer == 1:
      print('attractions:\n1=Shiti_Port\n2=Green_Island_Lighthouse\n') 
      choose = int(input('Choose where you want to go:'))
      if choose == 1:
        Shiti_Port_E()
      else :
        Green_Island_Lighthouse_E()
    if prefer == 2:
      print('attractions:\n1=Caogong_Taoist_Temple\n2=Liugui_Giant_Buddha\n')
      choose = int(input('Choose where you want to go:'))
      if choose == 1:
        Caogong_Taoist_Temple_E()
      else :
        Liugui_Giant_Buddha_E()
    if prefer == 3:
      print('attractions:\n1=Taichung_National_Opera\n')
      choose = int(input('Choose where you want to go:'))
      if choose == 1:
        Taichung_National_Opera_E()
    if prefer == 4:
      print('attractions:\n1=Raohe_Street_Night_Market\n2=Taitung_Tourist_Night_Market\n3=Liuhe_Tourist_Night_Market')
      choose = int(input('Choose where you want to go:'))
      if choose == 1:
        Raohe_Street_Night_Market_E()
      elif choose == 2:
        Taitung_Tourist_Night_Market_E
      else :
        Liuhe_Tourist_Night_Market_E
    if prefer == 5:
      print('attractions:\n1=Huoyan_Mountain_Trail\n2=Yuanzui_Shaolaishan_National_Trail\n')
      choose = int(input('Choose where you want to go:'))
      if choose == 1:
        Huoyan_Mountain_Trail_E()
      else :
        Yuanzui_Shaolaishan_National_Trail_E() 
    if prefer == 7:
      print('Estimated amount:',sum(Estimated_amount))
      break



print('謝謝使用')
