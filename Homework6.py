# "Условный оператор. Как работает оператор if."

x = 38
print ('дратути!')
if x < 0:
    print('Меньше нуля')
print('дотвидания!')

# примеры

a, b = 10, 5
if a > b:
    print('a > b')
if a > b and a > 0:
    print('успех 1')
if (a > b) and (a > 0 or b < 1000):
    print('успех 2')
if 5 < b and b < 10:
    print('успех 3')

# можно сравнивать - числа, строки, списки и т.д.
if '34' > '123':
    print('успех 4')
if '123' > '12':
    print('успех 5')
if [1, 2] > [1, 1]:
    print('успех 6')

# что нельзя сравнивать - разные типы

# if '6' > 5: # сравнение str и int выдаёт ошибку
#    print('успех 7')
# if [5, 6] > 5: # сравнение списка и int выдаёт ошибку
#    print('успех 8')

# но

if '6' != 5: # проверка на неравенство различных элементов допустима
    print('успех 9')