import os
import csv
def p(msg, *args):
    print(msg, args)

def menu():
 os.system('cls')
 p('=====歡迎使用記帳系統=====')
 p('功能列表:')
 p('        1. 紀錄花費')
 p('        2. 查詢紀錄')
 p('        3. 更改紀錄')

while True:
 menu()
 FUNCTION = int(input('請輸入您想進行的操作編號: '))
#紀錄花費
 if FUNCTION == 1:
    p('請輸入您要記錄的日期以及金額: ')
    month = int(input('月份: '))
    day = int(input('日期: '))
    money = int(input('請輸入要記帳的金額: '))
    #open必須給的參數:1.檔名 2.模式(read(r)、write(w)... 3.encoding，順序不可以換
    with open('money.csv',mode='a',newline='',encoding='utf-8') as file:
       writer = csv.writer(file)
       writer.writerow([month,day,money])
       p('資料已儲存')
       input('請輸入任意鍵繼續')
       menu()

 elif FUNCTION == 2:
   p('請輸入您要查詢的日期: ')
   month = input('月份: ')
   day = input('日期: ')
   with open('money.csv',mode='r',encoding='utf-8') as file:
      reader = csv.reader(file)
      for row in reader :
        if month in row[0] and day in row[1]:
           p('花費金額為:',row[2]) 
           input('請輸入任意鍵繼續')
           continue
        else :
           p('未找到您所查詢的日期之紀錄')
           input('請輸入任意鍵繼續')
           continue

 elif FUNCTION == 3:
    p('請輸入您要更改金額的日期')
    month = input('月份: ')
    day = input('日期: ')
    with open('money.csv',mode='r',encoding='utf-8') as file:
      reader = csv.reader(file)
      for row in reader :
        if month in row[0] and day in row[1]:
          p('目前記錄金額為: ',row[2])
          check = input('是否要更改金額，是請輸入"yes"，否則輸入"no": ')
          if check == "yes":
            money = int(input('請輸入要記帳的金額: '))
            with open('money.csv',mode='w',newline='',encoding='utf-8') as file:
             writer = csv.writer(file)
             writer.writerow([month,day,money])
             p('資料已儲存')
             input('請輸入任意鍵繼續')
             continue
          else:
            p('即將返回')
            input('請輸入任意鍵繼續')
            menu()
            continue
        else:
          p('未找到您所查詢的日期之紀錄')
          input('請輸入任意鍵繼續')
          menu()
          continue
