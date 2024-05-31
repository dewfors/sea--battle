from random import randint

from board import Board
from dot import Dot
from exceptions import BoardWrongShipException
from player import AI, User
from ship import Ship


class Game:
    def try_board(self):
        lens = [4, 3, 3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        try_count = 0
        for l in lens:
            while True:
                try_count += 1
                if try_count > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.start()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def __init__(self, size=9):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def greet(self):
        print("-------------------")
        print("  Вас приветствует  ")
        print("        игра       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def loop(self):
        num = 0
        while True:
            print("-" * 20)
            print("Доска пользователя:")
            print(self.us.board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.ai.board)
            print("-" * 20)
            if num % 2 == 0:
                print("Ходит пользователь!")
                print(f'Текущий счет: пользователь:компьютер - {self.ai.board.count}:{self.us.board.count}')
                repeat = self.us.move()
            else:
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 9:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.us.board.count == 9:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()
