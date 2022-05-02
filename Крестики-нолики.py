XY = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def pole():
    print(f'        ')
    print(f'  0 1 2')
    for i in range(3):
        print(f'{i} {XY[i][0]} {XY[i][1]} {XY[i][2]}')

def ask():
    while True:
        y = int(input('   Введите номер по оси Х от 0 до 2 '))
        x = int(input('   Введите номер по оси Y от 0 до 2 '))
        if (y == 0 or y == 1 or y == 2) and (x == 0 or x == 1 or x == 2):
            if XY[x][y] == " ":
                return x, y
            else:
                print('Ячейка занята')
        else:
            print('Введите число в диапазоне от 0 до 2')

def win():
    if XY[0][0] == XY[1][0] == XY[2][0] == 'X' or XY[0][0] == XY[0][1] == XY[0][2] == 'X' or XY[0][0] == XY[1][1] == XY[2][2] == 'X' or XY[0][1] == XY[1][1] == XY[2][1] == 'X' or XY[0][2] == XY[1][2] == XY[2][2] == 'X' or XY[1][0] == XY[1][1] == XY[1][2] == 'X' or XY[2][0] == XY[2][1] == XY[2][2] == 'X' or XY[2][0] == XY[1][1] == XY[0][2] == 'X':
        print('Игрок X выиграл')
        pole()
        return True
    if XY[0][0] == XY[1][0] == XY[2][0] == '0' or XY[0][0] == XY[0][1] == XY[0][2] == '0' or XY[0][0] == XY[1][1] == XY[2][2] == '0' or XY[0][1] == XY[1][1] == XY[2][1] == '0' or XY[0][2] == XY[1][2] == XY[2][2] == '0' or XY[1][0] == XY[1][1] == XY[1][2] == '0' or XY[2][0] == XY[2][1] == XY[2][2] == '0' or XY[2][0] == XY[1][1] == XY[0][2] == '0':
        print('Игрок 0 выиграл')
        pole()
        return True

i = 0
while True:
    i += 1
    pole()
    print('Ходит игрок X')
    x, y = ask()
    XY[x][y] = 'X'

    if win():
        break

    pole()
    print('Ходит игрок 0')
    x, y = ask()
    XY[x][y] = '0'

    if win():
        break

    if i == 8:
        print('Ничья')
        break




