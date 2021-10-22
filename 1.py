x = (1, 2, 3, 4, 5)
y = (3, 5, 6, 7, 8)
c = 0
c1 = 0
count_1 = 0
count_2 = 0
for i in x:
    count_1 += i
for i in y:
    count_2 += i
if count_1 > count_2:
    print('Сумма в кортеже 1 больше')
else:
    print('Сумма в кортеже 2 больше')
a = min(x)
b = min(y)
a1 = x.index(a)
b1 = y.index(b)
print(f'{a1},{b1} - номера минимальных значений кортежей первого'
      f' и второго соответсвтенного ')
for i in y:
    a = i * y[c]
    c += 1
    z.append(a)
for i in x:
    a = i * x[c1]
    c1 += 1
    z1.append(a)
print(z, z1)