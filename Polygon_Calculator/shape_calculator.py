
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        rectangle = ("*" * self.width + "\n") * self.height
        return rectangle

    def get_amount_inside(self, shape):
        max_width = self.width // shape.width
        max_height = self.height // shape.height
        return max_width * max_height

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)

    def __str__(self):
        return "Square(side={})".format(self.width)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

# picture = Rectangle(20,5)
# print(picture.get_picture())
