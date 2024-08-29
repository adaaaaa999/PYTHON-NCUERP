
a = [1,2,3,4]
user = int(input('數字: '))
#例外處理使得程式不會中斷(閃退)
try:
    print(a[user])
#會產生多個例外，就寫多個except
except IndexError :
    print('資料不存在')

#即使發生例外，依然會持續往下執行

# except Exception  可以捕捉所有例外，但會不知道是什麼例外導致中斷
#若要描述可用 except Exception as e:
# print('有例外:'str(e)
