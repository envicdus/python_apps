class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, width):
        self.height = height

    def get_area(self):
        return self.width * self.set_height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.set_height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if(self.width > 50 or self.height > 50):
            return "Too big for picture."
        string = (("*" * self.width) + "\n") * self.set_height
        return string

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())




class square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side
