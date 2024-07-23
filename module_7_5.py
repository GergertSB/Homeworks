'''
Лекция "Файлы в операционной системе".
'''

import os
import time

# print('Текущая директория:', os.getcwd()) # отображение пути к файлу в котором мы сейчас находимся
# if os.path.exists('Module_7'): # Если файл существует то True, иначе False
#     os.chdir('Module_7') # Если она есть то изменить её
# else:
#     os.mkdir('Module_7') # Создать директорию при её отсутствии
#     os.chdir('Module_7')
# print('Текущая директория:', os.getcwd())
#
# # os.makedirs(r'lesson\homework') # создание вложенных директорий
# print(os.listdir()) # получить список файлов в текущей директории
# for i in os.walk('.'):
#     print(i)
#
# os.chdir(r'D:\Python_01\Module') # сортировка содержимого директории
# print('Текущая директория:', os.getcwd())
# # print(os.listdir())
# file = [f for f in os.listdir() if os.path.isfile(f)] # сортировка файлов
# dirs = [d for d in os.listdir() if os.path.isdir(d)]# сортировка папок
# print(dirs)
# print(file)
# os.startfile(file[24]) # запуск файла по его номеру в списке
# print(os.stat(file[24])) # информация о файле
# print(os.stat(file[24]).st_size) # вывод только конкретной информации, например размер файла в байтах
# os.system('pip install random2')# установка библиотеки

'''
Домашнее задание по теме "Файлы в операционной системе".
'''

directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: '
            f'{formatted_time}, Родительская директория: {parent_dir}')
