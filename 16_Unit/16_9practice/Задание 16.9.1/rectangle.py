class Rectangle:
    def __init__(self,x ,y , width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_heigh(self):
        return self.height

    def get_description(self):
        return 'x={0}, y={1}, width={2}, height={3}'.format(self.x, self.y, self.width, self.height)

