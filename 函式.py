import os
def eq():
 a = int(input('請輸入一個數字: '))
 b = int(input('請輸入一個數字: '))
 c=a+b
 print(f'輸入數字的總和:',c)

while True:
 os.system('cls')
 eq()
 user = input('若要繼續可以輸入任意鍵，如果要退出可以輸入"quit" : ')
 if user == "quit":
  print('程式已結束')
  break
 else:
  continue
