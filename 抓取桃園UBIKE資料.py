import csv
import requests #透過pip3(pip 3.0)進行安裝，用於網路上抓資料
#網址是字串，需要加單引號
response = requests.get('https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=csv&limit=999')
#用.運算子可以直接使用裡面的程式碼(透過.叫出的函式，只屬於.前面的)，稱作"方法"。沒有.的函式，ex:print，叫做"函式"
#括號內=給予這個函式的參數，有多個參數要使用逗號區分開
#利用response收集這個網址回傳的資料，裡面是複合型資料
#寫上limit=999，才會回傳999筆資料(如網站資料大於999，則可將數字再調大)，否則他只會回傳一定的數量(可能不會全部的資料)

with open('ubike_v2.csv','w',encoding='utf-8') as file:#存到變數file裡面
    #open必須給的參數:1.檔名 2.模式(read(r)、write(w)... 3.encoding，順序不可以換
    file.write(response.text)
#寫text，response裡面的資料才會以text顯現
#w是寫入檔案，r是讀取檔案
#寫入編碼格式(在電腦看到、儲存的資料格式)utf-8(國際編碼)
#在程式中，每個字都有屬於它的編碼，假設沒有解碼，只會看到他的編碼，不會看到字
#這份檔案會寫入ubike_v2.csv(這份檔案不存在沒關係，因為是寫入，如果是讀取則需要是存在的)
#寫入之後，檔案會跑到左手邊的欄位

with open ('ubike_v2.csv','r',encoding='utf-8')as file:#存到變數file裡面
    result = csv.reader(file)
    #把file(大筆字串)根據"逗號位置"切割成一筆筆資料，存入result這個特殊櫃裡面
    #如果沒有這一行程式，在搜尋'中央大學'時，無法從大筆字串單獨找到中央大學，只能自己下去一個個找
    result = list(result)
    #把result做成list

    user = input('請輸入要搜尋的站台: ')

    for row in result: #row會隨著result的每一筆資料變動
        if user in row[3]: #找輸入的名稱，模糊搜尋
         print ('站名',row[3],'地址',row[6])
         print('  - 目前可借:', row[12])
         print('  - 目前空位:', row[5])
         print()