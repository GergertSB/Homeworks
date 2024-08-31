
def check_winner():
    if area[0][0] == "X" and area [0][1] == "X" and area [0][2] == "X":
        return "X"
    if area[1][0] == "X" and area [1][1] == "X" and area [1][2] == "X":
        return "X"
    if area[2][0] == "X" and area [2][1] == "X" and area [2][2] == "X":
        return "X"
    if area[0][0] == "X" and area [1][0] == "X" and area [2][0] == "X":
        return "X"
    if area[0][1] == "X" and area [1][1] == "X" and area [2][1] == "X":
        return "X"
    if area[0][2] == "X" and area [1][2] == "X" and area [2][2] == "X":
        return "X"
    if area[0][0] == "X" and area [1][1] == "X" and area [2][2] == "X":
        return "X"
    if area[0][2] == "X" and area [1][1] == "X" and area [2][0] == "X":
        return "X"
    if area[0][0] == "O" and area [0][1] == "O" and area [0][2] == "O":
        return "O"
    if area[1][0] == "O" and area [1][1] == "O" and area [1][2] == "O":
        return "O"
    if area[2][0] == "O" and area [2][1] == "O" and area [2][2] == "O":
        return "O"
    if area[0][0] == "O" and area [1][0] == "O" and area [2][0] == "O":
        return "O"
    if area[0][1] == "O" and area [1][1] == "O" and area [2][1] == "OX":
        return "O"
    if area[0][2] == "O" and area [1][2] == "O" and area [2][2] == "O":
        return "O"
    if area[0][0] == "O" and area [1][1] == "O" and area [2][2] == "O":
        return "O"
    if area[0][2] == "O" and area [1][1] == "O" and area [2][0] == "O":
        return "O"
    return "*"



def draw_area(): # функция для прорисовки игрового поля
    for i in area:
        print(*i)  # звездочка перед списком "распаковывает" его, убирает квадратные скобки.
    print()

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']] # составные части игрового поля
print('Добро пожаловать в крестики-нолики')
print('----------------------------------')
draw_area()
for turn in range(1, 10): # количество ходов 9
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = 'O'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')
    row = int(input('Введите номер строки (1, 2, 3) ')) - 1
    column = int(input('Введите номер столбца (1, 2, 3) ')) - 1
    if area[row][column] == '*': # проверка ячейки на отсутствие крестика или нолика
        area[row][column] = turn_char # Замена звездочки на крестик по введенным от пользователя значениям
    else:
        print('Ячейка уже занята, вы пропускаете ход')
        draw_area()
        continue
    draw_area()

    if check_winner() == 'X':
        print('Победа крестиков')
        break
    if check_winner() == 'O':
        print('Победа ноликов')
        break
    if check_winner() == '*' and turn == 9:
        print('Ничья')
        break