import math


class Parallelogram():
    '''A class to represent a Parallelogram'''

    def __init__(self, base, side, theta):
        '''(Parallelogram, float, float, float) -> NoneType
        Create a Parallelogram defined by the lengths of its two pairs of sides
        (base and side) and the interior angle (in degrees) between adjacent
        sides (theta).
        REQ: base, side, and theta are floats >= 0.
        REQ: theta represents the interior angle in degrees.
        '''
        # initialize four local variables
        self._base = base
        self._side = side
        self._theta = theta
        self._shape = 'Parallelogram'

    def area(self):
        '''(Parallelogram) -> float
        Returns the area of the Parallelogram.
        '''
        # convert the angle from degrees to radians
        self._angle = math.radians(self._theta)
        # calculate the area
        self._area = self._base * self._side * math.sin(self._angle)
        # return the area
        return self._area

    def bst(self):
        '''(Parallelogram) -> list
        Returns a list of three floats: [base, side, theta].
        '''
        # return the list
        return [self._base, self._side, self._theta]

    def __str__(self):
        '''(Parallelogram) -> str
        Returns a string representation of the Parallelogram.
        '''
        # create a string
        self._str = 'I am a ' + self._shape + ' with area ' + str(self.area())
        # return the string
        return self._str


class Rectangle(Parallelogram):
    '''A class to represent a Rectangle'''

    def __init__(self, base, side):
        '''(Rectangle, float, float) -> NoneType
        Create a Rectangle defined by the lengths of its two pairs of sides
        (base and side).
        REQ: base and side are floats >= 0.
        '''
        # call the parent constructor
        Parallelogram.__init__(self, base, side, 90)
        # update the shape
        self._shape = 'Rectangle'

    def area(self):
        '''(Rectangle) -> float
        Returns the area of the Rectangle.
        '''
        # call the parent function and return the area
        return Parallelogram.area(self)

    def bst(self):
        '''(Rectangle) -> list
        Returns a list of three floats: [base, side, 90].
        '''
        # call the parent function and return the list
        return Parallelogram.bst(self)

    def __str__(self):
        '''(Rectangle) -> str
        Returns a string representation of the Rectangle.
        '''
        # call the parent function and return the string
        return Parallelogram.__str__(self)


class Rhombus(Parallelogram):
    '''A class to represent a Rhombus'''

    def __init__(self, base, theta):
        '''(Rhombus, float, float) -> NoneType
        Create a Rhombus defined by the length of its sides (base) and the
        interior angle (in degrees) between adjacent sides (theta).
        REQ: base and theta are floats >= 0.
        REQ: theta represents the interior angle in degrees.
        '''
        # call the parent constructor
        Parallelogram.__init__(self, base, base, theta)
        # update the shape
        self._shape = 'Rhombus'

    def area(self):
        '''(Rhombus) -> float
        Returns the area of the Rhombus.
        '''
        # call the parent function and return the area
        return Parallelogram.area(self)

    def bst(self):
        '''(Rhombus) -> list
        Returns a list of three floats: [base, base, theta].
        '''
        # call the parent function and return the list
        return Parallelogram.bst(self)

    def __str__(self):
        '''(Rhombus) -> str
        Returns a string representation of the Rhombus.
        '''
        # call the parent function and return the string
        return Parallelogram.__str__(self)


class Square(Rectangle, Rhombus):
    '''A class to represent a Square'''

    def __init__(self, base):
        '''(Square, float) -> NoneType
        Create a Square defined by the length of its sides (base)
        REQ: base is a float >= 0.
        '''
        # call the parent constructors
        Rhombus.__init__(self, base, 90)
        Rectangle.__init__(self, base, base)
        # update the shape
        self._shape = 'Square'

    def area(self):
        '''(Square) -> float
        Returns the area of the Square.
        '''
        # call a parent function and return the area
        return Rectangle.area(self)

    def bst(self):
        '''(Square) -> list
        Returns a list of three floats: [base, base, 90].
        '''
        # call a parent function and return the list
        return Rhombus.bst(self)

    def __str__(self):
        '''(Square) -> str
        Returns a string representation of the Square.
        '''
        # call a parent function and return the string
        return Rectangle.__str__(self)
