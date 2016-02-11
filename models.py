import heapq
import math
import functools
from itertools import Counter
from functs import fullfills_needs


class Position:

    def __init__(self, r, c):
        self.r = r
        self.c = c

    def distance(self, that):
        return ((self.r - that.r) ** 2 + (self.c - that.c) ** 2) ** 0.5

class Warehouse(Position):

    def __init__(self, code, r, c, stock):
        super().__init__(r, c)
        self.code = code
        self.stock = stock

@functools.total_ordering
class Order(Position):

    def __init__(self, code, r, c, content):
        super().__init__(r, c)
        self.code = code
        self.content = content

    def weight(self):
        from main import SETTINGS
        return sum(amount * SETTINGS['products'][code].weight
                   for code, amount in enumerate(self.content))

    def products(self):
        from main import SETTINGS
        return [(SETTINGS['products'][code], amount)
                    for code, amount in enumerate(self.content)]

    def __lt__(self, other):
        return True

    def __eq__(self, other):
        return False

    def __repr__(self):
        return '(%d,%d) %s' % (self.r, self.c, self.content)


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

    def __init__(self, code, r, c):
        super().__init__(r, c)
        self.code = code
        self.commandqueue = []
        # Frequency table of products: Mapping product -> amount
        self.load = Counter()

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

    def load_weight(self):
        from main import SETTINGS
        return sum(amount * SETTINGS['products'][code].weight
                   for code, amount in enumerate(self.content))

    def add_load(self, product, amount=1):
        self.load[product] += amount
        if self.load_weight():
            self.load[product] -= amount
            raise ValueError('too much load')

    def clear_load(self)
        self.load = Counter()


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
    def __str__(self):
        return " ".join(map(str, ("D", self.order.code, self.product.code,
                self.count)))

class Load(MovingCommand):
    def __init__(self, warehouse, product, count):
        self.warehouse = warehouse
        self.product = product
        self.count = count
    def position(self):
        return self.warehouse
    def __str__(self):
        return " ".join(map(str, ("L", self.warehouse.code, self.product.code,
                self.count)))

class Unload(MovingCommand):
    def __init__(self, warehouse, product, count):
        self.warehouse = warehouse
        self.product = product
        self.count = count
    def position(self):
        return self.warehouse
    def __str__(self):
        return " ".join(map(str, ("U", self.warehouse.code, self.product.code,
                self.count)))

class Wait:
    def __init__(self, time):
        self._time = time
    def time(self, starting_position):
        return self._time
    def position(self):
        return None;
    def __str__(self):
        return " ".join(('W', str(self.time(None))))

class OrderQueue:
    def __init__(self, n_rows, n_cols, base_warehouse, orders):
        self.max_distance = (n_rows**2 + n_cols**2) ** .5
        self.base_warehouse = base_warehouse
        self.queue = [(self.priority(order), order) for order in orders]
        heapq.heapify(self.queue)

    def pop(self):
        priority, warehouse = heapq.heappop(self.queue)
        if priority == self.max_distance:
            raise IndexError
        return warehouse

    def priority(self, order):
        if fullfills_needs(order, self.base_warehouse):
            return order.distance(self.base_warehouse)

        return self.max_distance

    def __bool__(self):
        return self.empty()

    def empty(self):
        return len(self.queue) == 0

    def recalculate(self):
        heapq.heapify(self.queue)

    def __repr__(self):
        return repr(self.queue)
