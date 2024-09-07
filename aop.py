#oop由上而下擴充功能，aop切面擴充功能
def c(func):
    print('start')
    func()
    print('end')
    
@c
def base():
    print('我是小小程式')

print(base)
