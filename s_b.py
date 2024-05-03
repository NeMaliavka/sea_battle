MARK_NONE = '🔘 '
MARK_FALSE = '🟡 '
MARK_SHIP = '🔵 '
MARK_KILL = '🔻 '
MARK_MISS = '⚫ '
class Board:
    def __init__(self):
        self.game_board = self.create_board()

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

    def det_board(self):
        return self.game_board

    def set_pos(self, row: int, column: int, shape, pos: str = '_'):
        result = True
        if all([isinstance(row and column, int),
                1 <= row <= 6,
                1 <= column <= 6]
               ):
            for i in range(len(self.game_board)):
                if i == row-1 and result:
                    for j in range(len(self.game_board[i])):
                        if j == column - 1:
                            if self.game_board[i][j] == MARK_NONE:
                                self.game_board[i][j] = MARK_SHIP
                            else:
                                result = False
                                break
        else:
            result = False
        return result

    def set_area(self, row: int, column: int, shape: int, pos: str ='_'):
        if pos == '_':
            #print(self.game_board)
            for r in range(len(self.game_board)):
                if r == row - 1:
                    if r == 0:
                        for j in range(shape+2):
                            self.game_board[r+1][column+j-2] = MARK_FALSE
                    elif r == 5:
                        for j in range(shape+2):
                            self.game_board[r-1][column+j-2] = MARK_FALSE
                    else:
                        for j in range(shape+2):
                            self.game_board[r-1][column+j-2] = MARK_FALSE
                            self.game_board[r+1][column+j-2] = MARK_FALSE

        if pos == '|':
            #print(self.game_board)
            for l in range(len(self.game_board)):
                if '🔵 ' in self.game_board[l]:
                    ind = self.game_board[l].index('🔵 ')
                    if ind != 0 and ind != 5:
                        self.game_board[l][ind-1] = MARK_FALSE
                        self.game_board[l][ind+1] = MARK_FALSE
                    elif ind == 0:
                        self.game_board[l][ind+1] = MARK_FALSE
                    elif ind == 5:
                        self.game_board[l][ind-1] = MARK_FALSE

            # if row == 1:
            #     if column-1 == 0:
            #         self.game_board[row-1][column-1+shape] = MARK_FALSE
            #         for i in range(shape+1):
            #             self.game_board[row][column+i-1] = MARK_FALSE
            #     elif column == 6 - shape + 1:
            #         self.game_board[row-1][column-2] = MARK_FALSE
            #         for i in range(shape+1):
            #             self.game_board[row][column+i-2] = MARK_FALSE
            # elif row == 6:
            #     if column == 6:
            #         self.game_board[row-1][column-shape-1] = MARK_FALSE





                #     for i in range(shape+1):
                #         self.game_board[row][column+i-1] = MARK_FALSE
                # elif column == 6 - shape + 1:
                #     self.game_board[row+1][column-2] = MARK_FALSE
                #     for i in range(shape+1):
                #         self.game_board[row][column+i-2] = MARK_FALSE
    def __str__(self):
        return f' | 1 | 2 | 3 | 4 | 5 | 6 \n1|{"|".join(self.game_board[0])}' \
               f'\n2|{"|".join(self.game_board[1])}' \
               f'\n3|{"|".join(self.game_board[2])}' \
               f'\n4|{"|".join(self.game_board[3])}' \
               f'\n5|{"|".join(self.game_board[4])}' \
               f'\n6|{"|".join(self.game_board[5])}'

class Ship:
    def __init__(self):
        self.player_board = Board()
        self.long_ship = 1
        self.ship = 2
        self.small_ship = 4

    def create_ship(self, x: int, y: int, shape: int, pos: str = '_'):
        go = False
        if any([shape == 3 and self.long_ship != 0,
                shape == 2 and self.ship != 0,
                shape == 1 and self.small_ship != 0]):
            go = True
        # if shape == 3:
        #     if self.long_ship != 0:
        #         go = True
        # elif shape == 2:
        #     if self.ship != 0:
        #         go = True
        # elif shape == 1:
        #     if self.small_ship != 0:
        #         go = True
        if go:
            result = True
            if pos == '_':
                if y + shape - 1 <= 6:
                    for i in range(shape):
                        if result:
                            result = self.player_board.set_pos(x, y+i, shape, pos)
                        else:
                            break
                    if result:
                        print('Корабли успешно расположены, мой Капитан!')
                        self.player_board.set_area(x, y, shape, pos)
                        if shape == 3:
                            self.long_ship -= 1
                        elif shape == 2:
                            self.ship -= 1
                        elif shape == 1:
                            self.small_ship -= 1
                    else:
                        print('Надо бы пересмотреть тактику расположения кораблей...')
            elif pos == '|':
                if x + shape - 1 <= 6:
                    for i in range(shape):
                        if result:
                            result = self.player_board.set_pos(x+i, y, shape, pos)
                        else:
                            break
                    if result:
                        print('Корабли успешно расположены, мой Капитан!')
                        self.player_board.set_area(x, y, shape, pos)
                        if shape == 3:
                            self.long_ship -= 1
                        elif shape == 2:
                            self.ship -= 1
                        elif shape == 1:
                            self.small_ship -= 1
                    else:
                        print('Надо бы пересмотреть тактику расположения кораблей...')
        else:
            print('Каррамба! Что-то всё полетело к чертям! Сверься с курсом, ибо мы не можем выполнить этот приказ!')

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



