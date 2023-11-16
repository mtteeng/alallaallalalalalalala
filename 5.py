class Triangle:
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def types(self):
        if self.a == self.b == self.c:
            print('Равносторонний')
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            print('Равнобедренный')
        else:
            print('Разносторонний')

    def S(self):
        s = self.a * self.h // 2
        print(s)

t = Triangle(5, 6, 7, 9)
t.types()
t.S()
