def foo():
    print('start')
    t = yield 1
    print(f'contine: {t}')
    t1 = yield 2
    print(f'contine 2: {t1}')

y = foo()
print(y)

for i in y:
    print('=>',i)

