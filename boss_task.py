import time
print('Welcome')
time.sleep(3)
print('Ваша задача получить 4 литра воды используя вёдра объёмом 3 и 5 литров\n'
      'Вы можете использовать команды:\n'
      '1. "Наполнить_3" и "Наполнить_5" для наполнения соответствующего ведра\n'
      '2. "Опустошить_3" и "Опустошить_5" для того, чтобы вылить воду из соответсвующего ведра\n'
      '3. "Перелить_3_5" и "Перелить_5_3", чтобы переливать воду из одного ведра в другое\n'
      'Чтобы закончить игру досрочно - Стоп  ')
time.sleep(3)
com = input('Введите "Старт", чтобы начать')
count = 0
x_3 = 0
x_5 = 0
while x_5 >= 0:
      if x_5 == 4:
            print(f'Поздравляю, Вы прошли игру!! Количество операцияй - {count}')
            break
      com = input('Вводите команды! Удачи!')
      if com == 'Стоп':
            break
      if com == 'Наполнить_5':
            if x_5 == 5:
                  print('Ведро уже полное, попробуйте другую команду.')
            if x_5 == 0:
                  count += 1
                  x_5 += 5
                  print('Ведро на 5 литров наполнено')
                  print(f'В первом ведре {x_3}л')
                  print(f'Во втором ведре {x_5} л')
            if x_5  > 0 and x_5 < 5:
                  count += 1
                  print('Ведро дополнено до 5л')
                  x_5 = 5
                  print(f'В первом ведре {x_3}л')
                  print(f'Во втором ведре {x_5}л')

      if com == 'Наполнить_3':
            if x_3 == 3:
                  print('Ведро уже полное, попробуйте другую команду.')
                  print('В первом ведре 3л')
            if x_3 == 0:
                  count +=1
                  x_3 += 3
                  print('Ведро на 3 литра наполнено')
                  print(f'В первом ведре {x_3}л')
                  print(f'Во вотором ведре {x_5}л')
            if x_3 > 0 and x_3 < 3:
                  count += 1
                  print('Ведро дополнено до 3л')
                  x_3 = 3
                  print('В первом ведре 3л')
                  print(f'Во втором ведре {x_5}л')
      if com == 'Опустошить_3':
            if x_3 == 0:
                  print('Ведро и так пустое, попробуйте другую команду')
                  print('В первом ведре 0 литров')
            else:
                  count += 1
                  x_3 = 0
                  print('Ведро на 3 литра опустошено')
                  print('В первом ведре 0 литров')
            print(f'Во втором велре {x_5}л')
      if com == 'Опустошить_5':
            print(f'В первом ведре {x_3}л')
            if x_5 == 0:
                  print('Ведро и так пустое, попробуйте другую команду')
                  print('Во  втором ведре 0 литров')
            else:
                  count += 1
                  x_5 = 0
                  print('Ведро на 5 литров опустошено')
                  print('Во втором ведре 0 литров')
      if com == 'Перелить_3_5':
            if x_5 == 5:
                  print('Второе ведро полное, попробуйте другую команду')
            if x_3 == 0:
                  print('Ведро на 3л пустое - попробуйте сначала его наполнить')
            if x_3 > 0:
                  count += 1
                  if x_3 + x_5 <= 5:
                        x_5 = x_3 + x_5
                        print(f'Ведро на 5л наполнено на {x_3}л')
                        x_3 = 0
                        print('В первом ведре 0л')
                        print(f'Во втором ведре {x_5}л ')
                  if x_3 + x_5 > 5 and x_5 != 5:
                        if x_5 == 3:
                              x_3 -= 2
                              x_5 = 5
                              print(f'В первом ведре {x_3}л')
                              print('Во втором ведре 5л')
                        if x_5 == 4:
                              x_3 -= 1
                              x_5 = 5
                              print(f'В первом ведре {x_3}л')
                              print('Во втором ведре 5л')
      if com == 'Перелить_5_3':
            if x_3 == 3:
                  print('Первое ведро полное, попробуйте другую команду')
            if x_5 == 0:
                  print('Ведро на 5л пустое - попробуйте сначала его наполнить')
            if x_5 > 0:
                  count += 1
                  if x_3 + x_5 <= 3:
                        x_3 = x_3 + x_5
                        print(f'Ведро на 3л наполнено на {x_5}л')
                        x_5 = 0
                        print(f'В первом ведре {x_3}л')
                        print(f'Во втором ведре {x_5}л ')
                  if x_3 + x_5 > 3 and x_3 != 3:
                        c = 3 - x_3
                        if c >= x_5:
                              x_3 = x_5 + x_3
                              x_5 = 0
                              print(f'В превом ведре {x_3}л')
                              print(f'Во втором ведре {x_5}л')
                        if c < x_5:
                              x_3 = 3
                              x_5 = x_5 - c
                              print(f'В превом ведре {x_3}л')
                              print(f'Во втором ведре {x_5}л')

      if com != "Наполнить_3" and com != 'Наполнить_5' and com != 'Опустошить_3' \
              and com != 'Опустошить_5' and com != 'Перелить_3_5' and com != 'Перелить_5_3':
            print('Неверная команда')