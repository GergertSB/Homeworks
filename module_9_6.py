# Домашнее задание по теме "Генераторы"

'''
Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.

Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
'''

def all_variants(text):

    for f in range(len(text)):
        n = text[f]
        yield n
    for k in range(len(text)-1):
        m = text[k]
        p = text[k+1]
        yield m + p
    for d in range(len(text)):
        h = text[d]
        if h not in m+p:
            yield h + m + p


a = all_variants("abc")
for i in a:
    print(i)



# x = 0
    # y = 0
    # for x in range(len(text)):
    #     for y in range(x + 1, len(text) + 1):
    #         yield text[x:y]