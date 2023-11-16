class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def S(self):
        return self.x * self.y

    def P(self):
        return (self.x + self.y) * 2

s = Square(6, 8)
print(s.S(), s.P())