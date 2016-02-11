
class Position:

    def __init__(self, r, c):
        self.r = r
        self.c = c

    def distance(self, that):
        return ((self.r - that.r) ** 2 + (self.c - that.c) ** 2) ** 0.5

class Warehouse(Position):

    def __init__(self, r, c, stock):
        super().__init__(r, c)
        self.stock = stock

class Order(Position):

    def __init__(self, r, c, content):
        super().__init__(r, c)
        self.content = content

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

class Deliver:
    def __init__(self, order, product, count):
        self.order = order
        self.product = product
        self.count = count

class Load:
    def __init__(self, warehouse, product, count):
        self.warehouse = warehouse
        self.product = product
        self.count = count

class Unload:
    def __init__(self, warehouse, product, count):
        self.warehouse = warehouse
        self.product = product
        self.count = count

class Wait:
    def __init__(self, time):
        self.time = time

