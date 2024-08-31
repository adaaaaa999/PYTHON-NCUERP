def my_func (a):
    result= []
    for i in a:
        result.append(i ** 2) 
    return result

a = [2,8,6,5,10]

print(my_func(a))

def q3(a):
    return a**2

b= map(q3,a)#前面傳演算法，後面傳資料
print(b)