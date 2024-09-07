#定義輪廓 class類別，一個class可以有很多個object物件
#這個函式專屬於某種物體，則稱為"方法"，變數專屬於某種物體，稱為"屬性"

class Car:
    def __init__(self):#有__開頭不用主動呼叫，他會在建立物件的時候主動被呼叫
        self.color = '無色'
        print('我是__init__')
    def __str__(self):
        return f'我是車子{self.color}車子'
    def show(self):#把self當作沒有，但是一定得打，如果要傳參數可以逗號再加
        print(f'我是車子{self.color}')

a = Car() #建立物件
a.color = '紅色' #建立物件屬性，透過self抓得到，要注意屬性要建立在呼叫之前
a.show()#呼叫car物件的方法show

print(a)

