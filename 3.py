class Auto:

    def __init__(self, brand, model, year, meliage):
        self.brand = brand
        self.model = model
        self.year = year
        self.meliage = meliage

    def get_info(self):
        print(f'Марка = {self.brand}, Модель = {self.model}, Год выпуска = {self.year}, Пробег = {self.meliage}')

    def change(self, brand, model, year, meliage):
        self.brand = brand
        self.model = model
        self.year = year
        self.meliage = meliage

s = Auto('Lamborghini', 'Aventador', 2018, 30000)
# s.get_info()
s.change('Mercedes-Benz', 'G 63', 2013, 133000)
s.get_info()