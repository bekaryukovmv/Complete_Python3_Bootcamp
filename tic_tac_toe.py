import random
from IPython.display import clear_output

def display_board(board):
    """
    Функция рисующая и обновляющая игровое поле.
    Принимает на вход список маркеров. Ничего не возвращает
    """
    try:
        clear_output()
    except:
        print('\n'*100)
    print('-------------')
    print('|  ' + ' | ' + '  | ' + '  |')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print('|  ' + ' | ' + '  | ' + '  |')
    print('-------------')
    print('|  ' + ' | ' + '  | ' + '  |')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('|  ' + ' | ' + '  | ' + '  |')
    print('-------------')
    print('|  ' + ' | ' + '  | ' + '  |')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print('|  ' + ' | ' + '  | ' + '  |')
    print('-------------')


def player_input(player_1):
    '''
    Функция, принимающая пользовательский ввод. Служит для выбора маркера игры - крестика или нолика.
    Возвращает кортеж маркеров вида: (первый_игрок, второй_игрок)
    '''
    choice = '_'
    while choice not in ['X', 'x', 'o', 'O', 'о', 'О', 'х', 'Х']:
        choice = input(f'{player_1}, чем будете играть (Х или О)?: ')
    if choice in ['X', 'x', 'х', 'Х']:
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    '''
    Функция, размещающая маркер на поле и обновляющая доску.
    Принимает на вход доску, маркер и позицию маркера.
    Возвращает обновленную доску
    '''
    board[position] = marker
    return board


def win_check(board, mark):
    '''
    Функция, проверяющая выигрышный ли ход.
    Принимает на вход доску и маркер.
    Возвращает bool
    '''
    flag = False
    winners_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (3, 5, 7), (1, 5, 9)]
    for i in winners_combinations:
        if flag:
            break
        for j in i:
            if board[j] != mark:
                break
            continue
        else:
            flag = True
            break
    return flag


def choose_first(player_1, player_2):
    '''
    Случайным образом определяет кто из игроков ходит первым.
    Ничего не принимает на вход
    Возвращает строку с типа: "player_1"|"player_2"
    '''
    first = random.randint(1, 2)
    if first == 1:
        return player_1
    return player_2


def space_check(board, position):
    '''
    Определяет, свободна ли ячейка на игровом поле.
    Принимает на вход доску и номер игровой ячейки.
    Возвращает bool
    '''
    if position in range(1, 10):
        return board[position] == ' '
    else:
        return False


def full_board_check(board):
    '''
    Функция, определяющаяся заполненность доски.
    Принимает доску.
    Возвращает bool
    '''
    return ' ' not in board[1:]


def player_choice(board, player):
    '''
    Запрашивает у пользователя ячейку в которую он хочет поставить метку.
    Принимает на вход доску.
    Возвращает позицию.
    '''
    position = 0
    while (position not in range(1, 10)) and (not space_check(board, position)):
        position = int(input(f'Игрок {player}, выберите ячейку на поле (от 1 до 9): '))

    return position


def replay():
    '''
    Спрашивает у пользователяб хочет ли он сыграть еще раз.
    Возвращает bool
    '''
    ans = input('Хотите сыграть еще раз (да/нет)?: ')
    return ans.lower() in ['д', 'да', 'y', 'yes']


def one_game(turn, board, game_on, player_1, player_2, player_marker_1, player_marker_2):
    '''
    Функция, реализующая алгоритм одной игровой партии.
    Потучает на вход: turn, board, game_on, player_1, player_2, player_marker_1, player_marker_2.
    Ничего не возвращает.
    '''
    while game_on:
        # если права хода перешло к первому игроку
        if turn == player_1:
            display_board(board)
            position = player_choice(board, player_1)
            place_marker(board, player_marker_1, position)

            # Проверка на выигрыш
            if win_check(board, player_marker_1):
                display_board(board)
                print(f"{player_1}, Поздравляем! Вы выиграли!")
                game_on = False

            else:
                # Проверка, остались ли ещё ходы
                if full_board_check(board):
                    display_board(board)
                    print('Ходов больше нет. У вас ничья!')
                    break

                else:
                    # Переход хода ко второму игроку
                    turn = player_2

        else:
            # Если право хода перешло второму игроку
            display_board(board)
            position = player_choice(board, player_2)
            place_marker(board, player_marker_2, position)

            # Проверка на выигрыш
            if win_check(board, player_marker_2):
                display_board(board)
                print(f"{player_2}, Поздравляем! Вы выиграли!")
                game_on = False

            else:
                # Проверяет, осталось ли место на игровом поле
                if full_board_check(board):
                    display_board(board)
                    print('Ходов больше нет. У вас ничья!')
                    break

                else:
                    # Переход хода к первому игроку
                    turn = player_1


def play_game():
    '''
    Функция, управляющая процессом игры.
    Ничего не принимает на вход и ничего не возвращает.
    Запрашивает имена игроков и то, каким маркером они будут играть;
    разыгрывает очередность ходов, формирует пустое игровое поле,
    запрашивает готовность к игре
    и вызывает другие, необходимые функции.
    '''
    while True:
        print('Добро пожаловать на игру в Крестики-Нолики!')
        player_1 = input('Игрок 1, введите Ваше имя: ')
        player_2 = input('Игрок 2, введите Ваше имя: ')
        board = [' '] * 10
        player_marker_1, player_marker_2 = player_input(player_1)
        turn = choose_first(player_1, player_2)
        print(turn + ' Вы начинаете первым!')
        play_game = input('Готовы играть? да|нет ')
        if play_game.lower() in ['д', 'да', 'y', 'yes']:
            game_on = True
        else:
            game_on = False

        one_game(turn, board, game_on, player_1, player_2, player_marker_1, player_marker_2)

        if not replay():
            print('Спасибо за игру!')
            break


if __name__ == "__main__":
    play_game()
