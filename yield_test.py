data = []
def give_me_number():
    while True:
        user = input('number(離開=quit)=> ')
        if user=='quit':
            break
        else:
            yield int(user)
for i in give_me_number():
    data.append(i)

print(sum(data))