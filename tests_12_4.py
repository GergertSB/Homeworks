# Домашнее задание по теме "Логирование"

"""
Цель: получить опыт использования простейшего логирования совместно с тестами.

Задача "Логирование бегунов":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное значение в speed.

Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
Уровень - INFO
Режим - запись с заменой('w')
Название файла - runner_tests.log
Кодировка - UTF-8
Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.

Дополните методы тестирования в классе RunnerTest следующим образом:

test_walk:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте отрицательное значение в speed.
В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING
с сообщением "Неверная скорость для Runner".

test_run:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте что-то кроме строки в name.
В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING
с сообщением "Неверный тип данных для объекта Runner".
"""

import logging
import unittest
import rt_with_exceptions as re

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            hum1 = re.Runner('Степаныч', -2)
            hum1.walk()
            logging.info('"test_walk" выполнен успешно')

        except:
            logging.warning("Неверная скорость для Runner")


    def test_run(self):
        try:
            hum1 = re.Runner(444, 3)
            hum1.run()
            logging.info('"test_run" выполнен успешно')
    
        except:
            logging.warning("Неверный тип данных для объекта Runner")

if __name__ == '__main__':
    unittest.main()

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(funcName)s | %(levelname)s | %(message)s')
