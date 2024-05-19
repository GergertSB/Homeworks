# Задание "Средний балл":

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Average_ = sum(grades[0]) / len(grades[0])
Average_1 = sum(grades[1]) / len(grades[1])
Average_2 = sum(grades[2]) / len(grades[2])
Average_3 = sum(grades[3]) / len(grades[3])
Average_4 = sum(grades[4]) / len(grades[4])
# print(Average_, Average_1, Average_2, Average_3, Average_4)
list_ = sorted(students)
my_book = {list_[0]: Average_, list_[1]: Average_1,list_[2]: Average_2,list_[3]: Average_3,list_[4]: Average_4,}
# print(list_)
print(my_book)
