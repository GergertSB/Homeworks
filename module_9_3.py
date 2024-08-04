# Домашнее задание по теме "Генераторные сборки"

"""
Цель: понять механизм создания генераторных сборок и использования встроенных функций-генераторов.

Задача:
Дано 2 списка:
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
Необходимо создать 2 генераторных сборки:
"""

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i) - len(k) for i, k, in  zip(first, second) if len(i) != len(k))
second_result = (len(k) == len(n) for i in range(len(first)) for k, n in [(first[i], second[i])])



print(list(first_result))
print(list(second_result))