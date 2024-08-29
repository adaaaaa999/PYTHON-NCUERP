import csv

with open('臺北市立案一般護理之家一覽表.csv','r',encoding='utf-8',) as file :
#輸入要爬蟲的csv檔案，打開、使用模式、大多數文字書寫格式都是utf-8
    result = csv.reader(file) #讀取csv檔案
    result = list(result) #將csv檔案寫成list

    user = input('請輸入要查詢的區域: ')
    
    for row in result : #row會根據result的一筆筆資料變動
        if user in row[4] : #如果user輸入的資料有在row裡面，就會執行以下動作
            print ('機構名稱: ',row[2],' 開放床數: ',row[3],' 地址: ',row[4])
            print()
    
    user1 = input('若要查詢機構聯絡方式，請輸入機構名稱 : ')
    
    for row in result :
        if user1 in row[2] :
            print ('機構名稱: ',row[2],'機構聯絡號碼 : ',row[5])
