"""
STATUS: Working

OVERVIEW: Basic Shape calculator with inheritance

IMPROVEMENTS:
    - TODO Document
    - use modules
    - make it a cli
"""

# @ Imports

# * Defining


class shape_calculator:
    class Rectangle:

        def __init__(self, width, height):
            self.width = width
            self.height = height
            if width > 15:
                raise Exception('Too Big Dude!')

        def set_width(self, width):
            self.width = width

        def set_height(self, height):
            ''''''
            self.height = height

        def get_area(self):
            return self.width * self.height

        def get_perimeter(self):
            return (2 * self.width + 2 * self.height)

        def get_diagonal(self):
            return ((self.width ** 2 + self.height**2) ** 0.5)

        def get_picture(self):
            return (f"{'*  ' * self.width}\n" * self.height)

        def get_amount_inside(self, square):
            ''''''
            return (round(self.get_area()/square.get_area()))

        def __str__(self):
            return f"Rectangle(heigh={self.height}, width={self.width})"

    # child class
    class Square(Rectangle):

        def __init__(self, side):
            # call super() function
            self.side = side
            super().__init__(side, side)

        def set_side(self, side):
            self.width = side
            self.height = side

        def __str__(self):
            return f"Square(side={self.side})"


# ? Implementation
if __name__ == "__main__":
    rect = shape_calculator.Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = shape_calculator.Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(7)
    print(rect.get_amount_inside(sq))
