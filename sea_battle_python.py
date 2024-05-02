# Используя знания, полученные в данном модуле, напишите следующее приложение:
#
# Суть написанного приложения — игра «Морской бой».
# Интерфейс приложения должен представлять собой консольное окно с двумя полями 6х6 вида:
#     | 1 | 2 | 3 | 4 | 5 | 6|
# 1 | О | О | О | О | О | О |
# 2 | О | О | О | О | О | О |
# 3 | О | О | О | О | О | О |
# 4 | О | О | О | О | О | О |
# 5 | О | О | О | О | О | О |
# 6 | О | О | О | О | О | О |
# Игрок играет с компьютером. Компьютер делает ходы наугад, но не ходит по тем клеткам, в которые он уже сходил.
# Для представления корабля на игровой доске напишите класс Ship (в конструктор передаём информацию о его положении на доске).
# Опишите класс доски, на которую будут размещаться корабли.
# Корабли должны находится на расстоянии минимум одна клетка друг от друга.
# Корабли на доске должны отображаться следующим образом (пример):
#    | 1 | 2 | 3 | 4 | 5 | 6|
# 1 | ■ | ■ | ■ | О | О | О |
# 2 | О | О | О | О | ■ | ■ |
# 3 | О | О | О | О | О | О |
# 4 | ■ | О | ■ | О | ■ | О |
# 5 | О | О | О | О | ■ | О |
# 6 | ■ | О | ■ | О | О | О |
# На каждой доске (у ИИ и у игрока) должно находится следующее количество кораблей: 1 корабль на 3 клетки, 2 корабля на 2 клетки, 4 корабля на одну клетку.
# Запретите игроку стрелять в одну и ту же клетку несколько раз. При ошибках хода игрока должно возникать исключение.
#    | 1 | 2 | 3 | 4 | 5 | 6|
# 1 | X | X| X | О | О | О |
# 2 | О | О | О | О| X | X |
# 3 | О | T | О | О | О | О |
# 4 | ■ | О | ■ | О | ■ | О |
# 5 | О | О | О | О | ■ | О |
# 6 | ■ | О | ■ | О | О | О |
# В случае, если возникают непредвиденные ситуации, выбрасывать и обрабатывать исключения.
# Буквой X помечаются подбитые корабли, буквой T — промахи.
#
# Побеждает тот, кто быстрее всех разгромит корабли противника.
# class Dot:
#     def __init__(self):
#         self.x = None
#         self.y = None
#
#     def set_x(self, value):
#         if all([isinstance(value, int),
#                 1 <= value <= 6]):
#             self.x = value
#
#     def set_y(self, value):
#         if all([isinstance(value, int),
#                 1 <= value <= 6]):
#             self.y = value
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y #Выбрана занятая позиция
class MyException(Exception):
    pass


class Ship:
    def __init__(self, length=None, coord=None, direction=None, live=None):
        self.length = length
        self.coord_dot_nise_ship = coord
        self.direction = direction
        self.live = live

    def dots(self):
        '''возвращает список всех точек корабля'''
        pass


class Board:
    def __init__(self, hid=True):
        self.hid = hid
        self.game_board = self.start_playing_field()
        self.start_playing_field()
        self.lst_ships = None
        self.not_dead_ship = None

    def start_playing_field(self):
        field = {}
        for i in range(1, 7):
            for j in range(1, 7):
                el = (i, j)
                field[el] = 'O'
        return field

    def create_board(self):
        for i in range(0, 7):
            if i == 0:
                for j in range(0, 7):
                    if j == 0:
                        print(f' |', end=' ')
                    else:
                        print(f'{j}|', end=' ')
            else:
                print(f'{i}|', end='')
                for k in range(1, 7):
                    print(f' {self.game_board[(i,k)]}|', end='')
            print()

    def set_x_y_board(self, x: int, y: int, value: str):
        if all([isinstance(x, int),
                isinstance(y, int),
                1 <= x <= 6,
                1 <= y <= 6]):
            comb = (x, y)
            for key in self.game_board:
                if comb == key:
                    if self.game_board[key] == 'O':
                        self.game_board[key] = value
                    else:
                        print('Клетка занята')


class Player:
    def __init__(self):
        self.board = Board()
        self.enemy_board = Board(hid=False)

    def ask(self):
        '''«спрашивает» игрока, в какую клетку он делает выстрел.
        Пока мы делаем общий для AI и пользователя класс, этот метод
        мы описать не можем. Оставим этот метод пустым. Тем самым обозначим,
        что потомки должны реализовать этот метод.'''
        pass

    def move(self):
        '''Тут мы вызываем метод ask, делаем выстрел по вражеской доске
        (метод Board.shot), отлавливаем исключения, и если они есть,
        пытаемся повторить ход. Метод должен возвращать True, если этому
        игроку нужен повторный ход (например, если он выстрелом подбил
        корабль).'''

class User(Player):
    def __init__(self):
        Player.__init__()

    def ask(self):
        '''«спрашивает» игрока, в какую клетку он делает выстрел.
        Пока мы делаем общий для AI и пользователя класс, этот метод
        мы описать не можем. Оставим этот метод пустым. Тем самым обозначим,
        что потомки должны реализовать этот метод.'''
        pass


b = Board()

b.set_x_y_board(1, 1, 'x')
b.set_x_y_board(1, 2, 'x')
b.set_x_y_board(1, 2, 'x')
b.create_board()
