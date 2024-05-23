# "Цикл for. Элементы списка. Полезные функции в цикле"

mobile = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
for i in mobile:
    print(' Я езжу на автомобиле марки', [i])

# шаг два

mobile = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
cars_count = 0
for i in range(len(mobile)):
    cars_count += 10
    print(cars_count)
