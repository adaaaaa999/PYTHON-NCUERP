#有做例外處理，程式才不會被強制中斷(閃退)
try:
    user = int(input('請輸入數字: ')) #如果輸入無法轉型的字，例如英文字母，會直接跳到except做例外處理
    print('hello')
    print(user+3)
except ValueError:
    print('轉型失敗，請輸入正確的數字')

