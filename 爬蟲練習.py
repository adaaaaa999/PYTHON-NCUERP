import requests
from bs4 import BeautifulSoup

#爬取年代售票網的演唱會網頁
def crawl_web1():
    url = 'https://ticket.com.tw/application/UTK01/UTK0101_06.aspx?TYPE=1&CATEGORY=205'

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

    response = requests.get(url,headers=headers)
    print(response.text)
    print(response.status_code)
    with open('my-concert-01.html', 'w', encoding='utf-8', newline='') as file:
        file.write(response.text)
#crawl_web1()

#解析年代售票網，取得演唱會名稱和日期
def parse_web1():
    result = []
    with open('my-concert-01.html','r',encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(),'html.parser') #html.parser為內建解析器
        #把file讀出來丟入BeautifulSoup解析
        all_concerts = soup.find_all(class_='caption')
        for c in all_concerts:
            print('日期:',c.p.span.text)
            start = c.p.span.text.split('-')[0] #遇到"-"會切割資料，兩個日期都會成為第0筆
            print('開始時間: ',start)
            end = c.p.span.text.split('-')[-1] #但因為我想要取得後面那個日期，所以由後往前取
            print('結束時間: ',end)
            #另一種用判斷的: # c.p.span.text.split('-')[1] if len(c.p.span.text.split('-')) > 1 else start
            print('演唱會:',c.h4.text)
            print('內文:',c.div.text)
            print()

parse_web1()

