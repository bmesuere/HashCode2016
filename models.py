
import math

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
        self.commandqueue = []

    def ends_in(self):
        position = self
        time = 0
        for command in self.commandqueue:
            time += command.time(position)
            position = command.position() or position
        return (time, position)

    def ends_in_target(self, position):
        time, loc = self.ends_in()
        return time + position.distance(loc)


class MovingCommand:
    def time(self, starting_position):
        "The time to execute given the position"
        return 1 + math.ceil(self.position().distance(starting_position))

class Deliver(MovingCommand):
    def __init__(self, order, product, count):
        self.order = order
        self.product = product
        self.count = count
    def position(self):
        return self.order

class Load(MovingCommand):
    def __init__(self, warehouse, product, count):
        self.warehouse = warehouse
        self.product = product
        self.count = count
    def position(self):
        return self.warehouse

class Unload(MovingCommand):
    def __init__(self, warehouse, product, count):
        self.warehouse = warehouse
        self.product = product
        self.count = count
    def position(self):
        return self.warehouse

class Wait:
    def __init__(self, time):
        self._time = time
    def time(self, starting_position):
        return self._time
    def position(self):
        return None;
