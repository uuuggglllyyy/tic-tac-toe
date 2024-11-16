#тута печатаем игровое поле в консоль
def print_field(field):
    print("  0   1   2")
    for row_index, row in enumerate(field):
        print(row_index, end=" ")
        for cell in row:
            print(cell if cell else " ", "|", end=" ")
        print()

#тута проверяем, выиграл или нет
def check_win(field, player):
    for row in field:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(field[row][col] == player for row in range(3)):
            return True
    if all(field[i][i] == player for i in range(3)):
        return True
    if all(field[i][2 - i] == player for i in range(3)):
        return True
    return False

#если ничья
def check_draw(field):
    for row in field:
        for cell in row:
            if not cell:
                return False
    return True

#проверяем, является ли ход допустимым
def is_valid_move(field, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and field[row][col] is None


'''
а теперь собственно главная функция, она отвечает за:
1. Инициализацию игрового поля field размером 3x3.
2.  Установку текущего игрока current_player на "X".
3.  Запуск игрового цикла, который длится до тех пор, пока игра не завершится победой или ничьей.
4.  Отображение игрового поля на каждой итерации цикла с помощью функции print_field().
5.  Вывод сообщения о том, чей сейчас ход.
6.  Получение координат хода от пользователя и проверка их корректности с помощью функции is_valid_move().
7.  Обновление игрового поля с помощью полученных координат хода.
8.  Проверка победы или ничьей с помощью функций check_win() и check_draw() соответственно.
9.  Переключение текущего игрока на "O" или "X" в зависимости от того, чей был ход.
'''
def play_game():
    field = [[None] * 3 for _ in range(3)]
    current_player = "X"

    while True:
        print_field(field)
        print(f"Ход игрока {current_player}")

        while True:
            try:
                row, col = map(int, input("Введите координаты хода (строка, столбец, от 0 до 2): ").split(","))
                if is_valid_move(field, row, col):
                    field[row][col] = current_player
                    break
                else:
                    print("Некорректный ход. Попробуйте ещё раз.")
            except ValueError:
                print("Некорректный ввод. Введите числа через запятую.")

        if check_win(field, current_player):
            print_field(field)
            print(f"Игрок {current_player} победил!")
            break
        elif check_draw(field):
            print_field(field)
            print("Ничья!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()

