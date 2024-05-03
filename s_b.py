MARK_NONE = '🔘 '
MARK_FALSE = '🟡 '
MARK_SHIP = '🔵 '
MARK_KILL = '🔻 '
MARK_MISS = '⚫ '
class Block_ship:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class Board:
    def __init__(self, ships, hid: bool = True):
        self.game_board = self.create_board()
        self.ships = ships
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
        self.start_dot = (pos_x-1, pos_y-1)
        self.direction = direction
    


class Player:
    def __init__(self) -> None:
        self.player_board = Board()
       
p_1 = Ship()
p_1.create_ship(3, 6, 3, '|')
# p_1.create_ship(3, 4, 2, '|')
# p_1.create_ship(6, 6, 1)
# p_1.create_ship(1, 1, 1)
# p_1.create_ship(6, 1, 1)
# p_1.create_ship(5, 4, 2, '|')
# p_1.create_ship(3, 5, 2)
# p_1.create_ship(3, 1, 3)
# p_1.create_ship(3, 1, 3, '|')
print(p_1.player_board)



