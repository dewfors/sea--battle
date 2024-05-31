class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return 'Попытка выстрела за границы доски'


class BoardUsedException(BoardException):
    def __str__(self):
        return 'Вы уже стреляли в эту клетку'


class BoardWrongShipException(BoardException):
    pass



