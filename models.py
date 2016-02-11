
class Position:

    def __init__(self, r, c):
        self.r = r
        self.c = c

    def distance(self, that):
        return ((self.r - that.r) ** 2 + (self.c - that.c) ** 2) ** 0.5

class WareHouse(Position):

    def __init__(self, r, c):
        super().__init__(r, c)
        self.stock = dict()

class Order(Position):

    def __init__(self, r, c):
        super().__init__(r, c)
        self.content = dict()

class Product:

    def __init__(self, code, weight):
        self.code = code
        self.weight = weight

    def __eq__(self, other):
        return self.code == other.code

class Drone(Position):

    """ Position of drone is it's current location if the queue is empty
    or the last location if it's not.
    """

    def __init__(self, r, c):
        super().__init__(r, c)
        self.queue = []

