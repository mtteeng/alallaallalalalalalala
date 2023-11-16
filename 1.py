class Student:

    def __init__(self, name, last_name, age, score):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.score = score

    def get_info(self):
        print(f'name = {self.name}, last_name = {self.last_name}, age = {self.age}, score = {self.score}')

    def change(self, name, last_name, age, score):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.score = score

s = Student('Andrew', 'Zolotarev', 16, 4.9)
# s.get_info()
s.change('Pipa', 'Pipov', 21, 3)
s.get_info()