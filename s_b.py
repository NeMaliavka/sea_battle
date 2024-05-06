MARK_NONE = '🔘 '
MARK_FALSE = '🟡 '
MARK_SHIP = '🔵 '
MARK_KILL = '🔻 '
MARK_MISS = '⚫ '


class PosError(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        print(f': {error}')


class Block_ship:
    def __init__(self, x: int, y: int) -> None:
        self.x = None
        self.y = None
        self.check_pos(x, y)

    def check_pos(self, x, y):
        if all([0 <= x <= 5,
                0 <= y <= 5]):
            self.x = x
            self.y = y
            print("Ok")
        else:
            return 'Каррамба! Капитан, ты напутал с координатами и всё полетело в ТарТарары!'


class Board:
    def __init__(self, hid: bool = True):
        self.game_board = self.create_board()
        self.ships = {3: 1, 2: 2, 1: 4}
        self.good_ships = 6
        self.hid = hid

    def get_game_board(self):
        return self.game_board

    def create_board(self):
        field = []
        for i in range(1, 7):
            row = []
            for j in range(1, 7):
                row.append(MARK_NONE)
            field.append(row)
        return field

    def get_board(self):
        return self.game_board

    def add_ship(self, block, direction, size_ship):

        if direction == '|' and self.ships[size_ship] != 0:
            if block[0] + size_ship - 1 <= 6:
                buffer_zone = []
                for i in range(size_ship):
                    if self.game_board[block[0]+i][block[1]] == MARK_NONE:
                        self.game_board[block[0] + i][block[1]] = MARK_SHIP
                        buffer_zone.append((block[0]+i, block[1]))
                    else:
                        return 'Капитан, данная позиция уже занята другим кораблём!'
            else:
                return 'Капитан, мы не можем выполнить Ваш приказ! Корабль не может встать на эту позицию'
            self.ships[size_ship] -= 1
            self.contour(buffer_zone)
            print(f'кораблей с {size_ship} можно разместить еще {self.ships[size_ship]}')
        elif direction == '-' and self.ships[size_ship] != 0:
            if block[1] + size_ship - 1 <= 6:
                buffer_zone = []
                for i in range(size_ship):
                    if self.game_board[block[0]][block[1]+i] == MARK_NONE:
                        self.game_board[block[0]][block[1]+i] = MARK_SHIP
                        buffer_zone.append((block[0], block[1]+i))
                    else:
                        return 'Капитан, данная позиция уже занята другим кораблём!'
            else:
                return 'Капитан, мы не можем выполнить Ваш приказ! Корабль не может встать на эту позицию'
            self.ships[size_ship] -= 1
            self.contour(buffer_zone)
            print(f'кораблей с {size_ship} можно разместить еще {self.ships[size_ship]}')
        else:
            return 'Капитан, у нас больше нет таких кораблей...'

    def contour(self, ships: list):
        pass

    def __str__(self):
        return f' | 1 | 2 | 3 | 4 | 5 | 6 \n1|{"|".join(self.game_board[0])}' \
               f'\n2|{"|".join(self.game_board[1])}' \
               f'\n3|{"|".join(self.game_board[2])}' \
               f'\n4|{"|".join(self.game_board[3])}' \
               f'\n5|{"|".join(self.game_board[4])}' \
               f'\n6|{"|".join(self.game_board[5])}'


class Ship:
    def __init__(self, size: int, pos_x: int, pos_y: int, direction: str):
        self.size = size
        self.start_dot = (pos_x - 1, pos_y - 1)
        self.direction = direction


class Player:
    def __init__(self) -> None:
        self.player_board = Board()


# p_1 = Ship()
# p_1.create_ship(3, 6, 3, '|')
# p_1.create_ship(3, 4, 2, '|')
# p_1.create_ship(6, 6, 1)
# p_1.create_ship(1, 1, 1)
# p_1.create_ship(6, 1, 1)
# p_1.create_ship(5, 4, 2, '|')
# p_1.create_ship(3, 5, 2)
# p_1.create_ship(3, 1, 3)
# p_1.create_ship(3, 1, 3, '|')

dot = Block_ship(0, 5)
# print(dot.y, dot.x)
game = Board()
print(game.add_ship((dot.x, dot.y), '|', 3))
print(game)
dot2 = Block_ship(0, 5)
print(game.add_ship((dot2.x, dot2.y), '|', 2))
print(game)
dot3 = Block_ship(0, 0)
game.add_ship((dot3.x, dot3.y), '-', 2)
print(game)
