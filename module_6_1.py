# Домашнее задание по теме "Зачем нужно наследование"
# Задача "Съедобное, несъедобное":
"""
Разнообразие животного мира давно будоражит умы человечества. Царства, классы, виды... Почему бы и нам не попробовать
выстроить что-то подобное используя наследования классов?
Необходимо описать пример иерархии животного мира, используя классы и принцип наследования.
"""

class Animal:
    def __init__(self, name):
        self.alive = True # живой или не живой
        self.fed = False # голодный или сытый
        self.name = name


    def eat(self, food): # Результат поедания чего ли-бо
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False  # съедобное или не съедобное


# Определение классов-наследников для Animal
class Mammal(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

class Predator(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__(name)


# Определение классов-наследников для Plant
class Flower(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = False

class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True

# Создание объектов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Вывод информации и тестирование методов
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.