class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Dot({self.x}, {self.y})'


if __name__ == '__main__':
    a = Dot(1, 2)
    b = Dot(1, 2)
    d = Dot(2, 2)
    print(a == b)
    print(a == d)




