import random
def get_3_random_number():
    index=0
    while index<3:
     yield random.randint(0,10)
     index +=1

data = []
for i in get_3_random_number():
   data.append(i)

print(data,sum(data))

#data = list(get_3_random_number())  #list會自動把裡面資料一筆筆抓出來
#print(data,sum(data))

