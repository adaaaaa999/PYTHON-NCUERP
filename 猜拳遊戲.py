import random
for i in range(100):
 try:
    user = int(input('請問是否要玩猜拳，要的話請輸入1，不要請輸入2: '))
    if user == 2:
        print('歡迎下次再玩')
        break
    elif user ==1:
        print('0為剪刀，1為石頭，2為布')
        pc = random.randint(0,2) #0剪刀 1石頭 2布
#random.randint需要給範圍
        user = int(input('請出拳:'))
        if user<0 or user>2:
            print('你是不是按錯了:) 請重新選擇是否要玩遊戲')
            continue
        print(f'電腦出拳 :{['剪刀','石頭','布'][pc]}')
        if pc == user:
            print('平手')
        elif pc==0 and user==1:
            print('你贏了')
        elif pc==0 and user==2:
            print('你輸了')
        elif pc==1 and user==0:
            print('你輸了')
        elif pc==1 and user==2:
            print('你贏了')
        elif pc==2 and user==0:
            print('你贏了')
        elif pc==2 and user==1:
            print('你輸了')
 except ValueError:
     print('不可輸入非數字，請重新選擇')


