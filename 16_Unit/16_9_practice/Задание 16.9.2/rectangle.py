class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return 'Длина - {0}, Ширина - {1}, Площадь - {2}'.format(self.x, self.y, self.x * self.y)


rect = Rectangle(5, 10)
print(rect.get_area())
