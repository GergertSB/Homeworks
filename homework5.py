# Работа со списками

my_list = ['apple', 'kiwi', 'banana', 'mango', 'apricot', 'coconut']
print(my_list)
print(my_list[0], my_list[5])
print(my_list[3:6])
my_list[3] = 'peach'
print(my_list)

# работа со славарями

my_dict = {'apple': 'яблоко', 'kiwi': 'киви', 'banana': 'банан', \
           'mango': 'манго', 'apricot': 'абрикос', 'coconut': 'кокос'}
print(my_dict)
print(my_dict['banana'])
my_dict.update({'peach': 'персик'})
print(my_dict)