import requests
import json#json是一種資料格式
#json的資料格式有2種:
# 1. 物件(object): 一般用大括號{}表示
# 2. 陣列(array): 一般用中括號[]表示
resp = requests.get('https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&ed=20240914&geo=TW&hl=zh-TW&ns=15')

# print(resp.text)
# print(resp.status_code)

all_data = json.loads(resp.text.replace(')]}\',', ''))#將json格式的資料轉換成python的資料
#因為我們使用的API前面有一些非JSON格式的文字，所以我們在轉換資料格式時，先將前面的文字replace成空白

# 拿到今天所有搜尋排名
all_search = all_data['default']['trendingSearchesDays'][0]['trendingSearches']

for s in all_search:
    print(f'{s['title']['query']}: {s['formattedTraffic']}')
