#yield 迭代 (一筆一筆取資料)，為for in迴圈的原理
#有yield之後，foo()就不會是函式，而是一個產生器

def foo():#產生器會呼叫裡面要做的事情，輸入next(y)會呼叫產生器
    print('start')
    t = yield 1#遇到yield相當於暫停，需要再輸入一次next(y)再呼叫一次產生器才會繼續進行
    print(f'contine: {t}')
    t1 = yield 2#如果想要顯示yield裡面的值，需要用print
    print(f'contine 2: {t1}')

y = foo()#為產生器，呼叫foo時會回傳值給y
print(y)#打這個不會有裡面的東西，只會回傳產生器foo()，而不會執行裡面的東西

print('開始執行產生器')
a = next(y)#有這個產生器才會執行，但中間遇到yield就會暫停，就會需要再打next(y)去呼叫產生器
print(a)#上面執行後，會回傳1這個值到a，那我們需要print出來他才會顯示
b=y.send('yes')#可以使用send觸發繼續執行，遇到yield依然會暫停，差別是會把send後面的值回傳
print(b)
next(y)

