# Самостоятельная работа по уроку "Распаковка параметров и параметры функции"

# 1. Функция с параметрами по умолчанию:
def print_params(a=1, b="строка", c=True): # функция с заданными по умолчанию параметрами
    print(a, b, c) # при вызове функции вывести на экран

print_params() # отображаются заданные по умолчанию значения
print_params(2, 2, 2) # параметры успешно заменились на указанные
print_params(b=25) # замена пораметра и со строки на число
print_params(c=[1,2,3]) # замена параметра с Булева значения на список

# 2.Распаковка параметров:

values_list = [5, 'список', True]
values_dict = {'a': 8, 'b': 'перечень', 'c': True}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42) # Да будет работать, потому что количество вызываемых параметров не превышает\
                                # их количество в функции