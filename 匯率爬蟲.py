#依資料來源不同分類 1.靜態(直接抓網站的東西) 2.API(跟後端溝通要來的資料) 3.動態(需要輸入資料)
#HTML 僅是網頁資料的內容，外觀由css做
#<section> 你好 </section> (section為標籤，你好為標籤內容)
#<section id="3"> 嗨 </section> (空格+""為屬性)
#CSS
#<a class="btn hee"> class是css的樣式，資料要不要斜體、粗體、多大、顏色等等樣子都是由css製作
from bs4 import BeautifulSoup
import requests #用requests抓下來，由beatuifulsoup解析
response = requests.get('https://rate.bot.com.tw/xrt?Lang=zh-TW')
print('狀態碼',response.status_code)#狀態碼(找不到=404，沒有權限=3**，有成功=2**，網站掛了或有問題=5**)

soup = BeautifulSoup(response.text,'html.parser') #解析網站，html.parser為py內建
#會幫我們轉換成python的資料架構: 包含字典、清單、物件

#取得標籤內容，這個只能拿到第一個出現的標籤
print(soup.p.text)#拿到解析網站後的title標籤 +text就是拿title裡面的文字

#取得標籤屬性，以下兩種方式都可以拿到
print(soup.a.attrs['href'])#attrs是a標籤內所有屬性形成的字典
print(soup.a.get('href'))

#巢狀，標籤可以包住其他標籤，如下:
#<body>
# <a> 為body的子標籤
# </a>
#<body>

#取得較裡面的標籤(這方法只能都取得第一個該名標籤)
print(soup.table.tr.text)

#find() 只會回傳第一個
#find_all()會回傳全部
all_tr = soup.tbody.find_all('tr')#找tbody裡面所有的tr標籤
for tr in all_tr:
    #print(tr.td.div.div.img.attrs['alt'])
    #讀取幣別文字
    divs = tr.td.div.find_all('div')
    print(divs[1].text.strip())#strip移除後面的換行符號和空格

    tds = tr.find_all('td')#找tr裡面所有的td標籤並且形成字典
    print('現金買入:',tds[1].text)#列出td標籤字典裡的第二項
    print('現今賣出:',tds[2].text)
    print('即期買入:',tds[3].text.strip())
    print('即期賣出:',tds[4].text.strip())

    #直接用屬性值
    cash_buy = tr.find(attrs = {'data-table':'本行現金買入'})#find只會找第一筆符合的資料，即使後面有重複的也抓不到
    print(cash_buy.text)

#(較為精簡)直接用屬性值，示範2:(若有"-"符號，則無法使用，因為py不支援這個符號)
imgs = soup.find_all(title='幣別國旗')
for i in imgs:
    print(i.attrs['src'])




