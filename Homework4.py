immutable_var = 'apple', True, 1, 4.5
print(immutable_var)
# immutable_var[0][0] = 'banane' # объект данного типа не поддерживает изменение элемента
print(immutable_var)
mutable_list = ['cherry', False, 5]
print(mutable_list)
mutable_list[1] = 'Urban'
print(mutable_list)