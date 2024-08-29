#while 無窮迴圈，藉由條件是否成立決定程式是否可以進行，請記得需要有能停止的條件
#可搭配break

import random

a = ['0','1','2','3','4','5','6','7','8','9']

answer = random.sample(a,4) #使用randint會出現重複
answer = answer[0] + answer[1] + answer[2] + answer[3]
print (answer)

gc = 0 #紀錄猜測次數

while True:
    user = input('請猜0~9之間的四位數(不可以重複): ')
    gc +=1 #次數加1

    try:
        int(user)
    except ValueError:
        print ('只能輸入數字，請重新輸入')
        continue

    if len(user) !=4:
        print('只能輸入四個數字，請重新輸入')
        continue

    if len(set(user)) != 4:
        print('數字不可重覆, 請重新輸入')
        continue

    if user == answer:
        print(f'猜對了，總共猜了{gc}次')
        break
    how_many_A = 0
    if answer[0] == user[0]:
        how_many_A+=1
    if answer[1] == user[1]:
        how_many_A+=1
    if answer[2] == user[2]:
        how_many_A+=1
    if answer[3] == user[3]:
        how_many_A+=1
        

    how_many_B = 0
    if user[0] in answer and user[0] != answer[0]:
        how_many_B += 1

    if user[1] in answer and user[1] != answer[1]:
        how_many_B += 1

    if user[2] in answer and user[2] != answer[2]:
        how_many_B += 1

    if user[3] in answer and user[3] != answer[3]:
        how_many_B += 1
    
    print(f'{how_many_A}A{how_many_B}B')


        
