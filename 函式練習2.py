def show(name, age, phone, addr, birth):
    if addr == '':
        return "無資料"
    print(f'姓名: {name}, 年齡: {age}, 電話: {phone}, 地址: {addr}, 生日: {birth}')


show('aaron', 19, '0987654321', 'xxxx', '2000-01-01')
show('andy', 99, '0987654333', 'dsfsdxxxx', '2001-01-01')
show('apple', 99, '0987654333')
show('abner', 99, '0987654333')