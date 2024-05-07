import random
from abc import ABC, abstractmethod
MARK_NONE = '🔘 '
MARK_BUFFER = '🟡 '
MARK_SHIP = '🔵 '
MARK_KILL = '🔻 '
MARK_MISS = '⚫ '


class PosError(Exception):
    pass

class PosOutError(PosError):
    def __str__(self):
        return 'Каррамба! За пределы моря не стреляем! Таков морской закон!'


class PosRepidError(PosError):
    def __str__(self):
        return "Капитан, мы уже стреляли по этим координатам..."


class Block_ship:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        # self.check_pos(x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'pos x -> {self.x} \npos y -> {self.y}'

    # def check_pos(self, x, y):
    #     if all([1 <= x <= 6,
    #             1 <= y <= 6]):
    #         self.x = x
    #         self.y = y
    #         print("Ok")
    #     else:
    #         return 'Каррамба! Капитан, ты напутал с координатами и всё полетело в ТарТарары!'

class Ship:
    def __init__(self, size: int, block_ship: Block_ship, direction: str):
        self.size = size
        self.start_dot = block_ship
        self.direction = direction
        self.lives = size

        self.ship_blocks = []
        for i in range(self.size):
            pos_x = self.start_dot.x
            pos_y = self.start_dot.y

            if self.direction == '|':
                pos_x += i
            elif self.direction == '-':
                pos_y += i

            self.ship_blocks.append(Block_ship(pos_x, pos_y))

class Board:
    def __init__(self, hid: bool = False, size: int = 6):
        self.count = 0
        self.busy = [] # список занятых точек на доске
        self.ships = [] # список кораблей на поле
        self.hid = hid
        self.size_board = size
        self.game_board = self.create_board()

    def get_game_board(self):
        return self.game_board

    def create_board(self):
        field = []
        for i in range(self.size_board):
            row = []
            for j in range(self.size_board):
                row.append(MARK_NONE)
            field.append(row)
        return field

    def get_board(self):
        return self.game_board

    def add_ship(self, ship: Ship):
        for d in ship.ship_blocks:
            if self.out(d) or d in self.busy:
                raise PosError
        for d in ship.ship_blocks:
            self.game_board[d.x][d.y] = MARK_SHIP
            self.busy.append(d)
        self.ships.append(ship)
        self.coutour(ship)

    def coutour(self, ship: Ship, verb: bool = True):
        n = [
            (-1, -1), (-1, 0), (-1, 1),
            (0,-1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]
        for d in ship.ship_blocks:
            for dx, dy in n:
                current = Block_ship(d.x + dx, d.y + dy)
                if not(self.out(current)) and current not in self.busy:
                    #self.game_board[current.x][current.y] = MARK_BUFFER
                    if verb:
                        self.game_board[current.x][current.y] = MARK_BUFFER
                    self.busy.append(current)

    def out(self, dot: Block_ship):
        return not((0 <= dot.x < self.size_board) and (0 <= dot.y < self.size_board))

    def attack(self, dot: Block_ship):
        if self.out(dot):
            raise PosOutError

        if dot in self.busy:
            raise PosRepidError

        self.busy.append(dot)

        for ship in self.ships:
            if dot in ship.ship_blocks:
                ship.lives -= 1
                self.game_board[dot.x][dot.y] = MARK_KILL
                if ship.lives == 0:
                    print('Аррра! Корабль уничтожен!')
                    self.count += 1
                    self.coutour(ship, verb=True)
                    return False
                else:
                    print('Судно подбито!')
                    return True
        self.game_board[dot.x][dot.y] = MARK_MISS
        print('Не судьба, снаряд теперь покоится на дне моря...')
        return False

    def begin(self):
        self.busy = []

    def __str__(self):
        res = '    '
        for i in range(self.size_board):
            res += str(i+1) + '|  '
        res += '\n'
        count = 1
        for i in range(self.size_board):
            res += str(count)+'|'+"|".join(self.game_board[i]) + '|' + '\n'
            count += 1
        if self.hid:
            res = res.replace(MARK_SHIP, MARK_NONE)
            res = res.replace(MARK_BUFFER, MARK_NONE)
        return res

class Player(ABC):
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    @abstractmethod
    def ask(self):
        '''Запросить данные для создания/размещения корабля'''
        pass

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.attack(target)
                return repeat
            except PosError as e:
                print(e)

class Computer(Player):
    def ask(self):
        dot = Block_ship(random.randint(0, self.board.size_board - 1), random.randint(0, self.board.size_board - 1))
        print(f'Наш противник отправился в координаты: {dot.x} {dot.y}')
        return dot

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.attack(target)
                return repeat
            except PosError as e:
                pass

class User(Player):
    def ask(self):
        while True:
            coords = input('Куда отправимся, мой капитан: ').split()
            if len(coords) != 2:
                print('Нужны 2 координаты')
                continue
            x, y = coords

            try:
                x, y = int(x), int(y)
            except:
                print('Мой капитан, введи числами')
                continue
            return Block_ship(x-1, y-1)


class Game:
    def __init__(self, size=6):
        self.start_text()
        self.size_board = size
        player_board = self.player_create_board()
        computer_board = self.enemy_board()
        computer_board.hid = True

        self.player = User(player_board, computer_board)
        self.computer = Computer(computer_board, player_board)

    def player_create_board(self):
        ships = [3, 2, 2, 1, 1, 1, 1]
        game_board = Board(size=self.size_board)
        while len(ships) != 0:
            posX, posY = input('Капитан, введи координаты для расстановки корабля: ').split()
            size_ship = input('Сударь, введи размер корабля: ')
            try:
                posX, posY, size_ship = int(posX), int(posY), int(size_ship)
            except:
                print('Протри моргала, отсавь ром и попробуй ещё раз')
                continue
            direction = input('Укажи как расположить корабль (| или -): ')
            if '|' not in direction and '-' not in direction:
                print('Капитан, проспись и попробуй ещё раз...')
                continue
            if size_ship not in ships:
                print('Старый ты черт, такой корабль мы не можем себе позволить! Пробуем ещё раз!')
                continue
            ship = Ship(size_ship, Block_ship(posX-1, posY-1), direction)
            try:
                game_board.add_ship(ship)
                ships.remove(size_ship)
                print('Карабль на своей позиции!')
                print(game_board)
            except PosError:
                pass
        game_board.begin()
        return game_board

    def create_board(self):
        ships = [3, 2, 2, 1, 1, 1, 1]
        game_board = Board(size=self.size_board)
        check = 0
        for ship in ships:
            while True:
                check += 1
                if check > 200:
                    return None
                s = Ship(ship, Block_ship(random.randint(0, self.size_board), random.randint(0, self.size_board)), random.choice(['|', '-']))
                try:
                    game_board.add_ship(s)
                    break
                except PosError:
                    pass
        game_board.begin()
        return game_board

    def enemy_board(self):
        board = None
        while board is None:
            board = self.create_board()
        return board

    def game_process(self):
        num = 0
        while True:
            print(' - 🏴‍☠️ - 🏴‍☠️ - 🏴‍☠️ ')
            print('Доска Капитана:')
            print(self.player.board)
            print(' - 🤖 - 🤖 - 🤖')
            print('Доска противника:')
            print(self.computer.board)
            if num % 2 == 0:
                print('Капитан рулит')
                game_is_on = self.player.move()
            else:
                game_is_on = self.computer.move()
            if game_is_on:
                num -= 1

            if self.computer.board.count > 6:
                print('Тысяча чертей! Каптан одолел морских дъяволов!')
                break
            if self.player.board.count > 6:
                print('Палундрааа! Мы тонем!')
                break

            num += 1

    def start_text(self):
        hello_text = '''
\tКарррамба!
Приветствую тебя, мой капитан!
Ты готов отправиться в путь, в увлекательное морское путешествие с оглушающим залпом пушек?
Конечно готов! К чему эти вопросы, якорь мне под палубу!
Запомни, морской ты чёрт, для управления ты должен передавать направление:
широту и долготу, без них мы бессильны.
Помни же, сначала передаешь информацию о координатах Х,
а потом уже Y, и да поцелует меня русалка, все эти морские крысы пойдут ко дню.
Тащите рому, бездельники, Капитан у штурвала!\n'''
        print(hello_text)


g = Game()
g.game_process()


