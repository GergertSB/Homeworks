# Самостоятельная работа по уроку "Рекурсия"
# Задача "Рекурсивное умножение цифр":

def get_multiplied_digits(number): # функция с параметром
    str_number = str(number) # строковое представление параметра
    first = int(str_number[0]) # переменная с первым символом
    if len(str_number) > 1: # если длинна больше одного символа
        return first * get_multiplied_digits(int(str_number[1:])) # возврат значение в str_number
    else:
        return first


result = get_multiplied_digits(40203)

print(result)
