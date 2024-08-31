def my_filter(a):
    result = []

    #for i in a:
     #   if i % 2 == 0:
      #      result.append(i)

    return result

a = [2, 7, 13, 24, 98, 101]

print(my_filter(a))

def q1(a):
    return a % 2 == 0

def q2(a):
    return a >= 60

print(list(filter(q1, a)))
print(list(filter(q2, a)))