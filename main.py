from collections import Counter
from models import *
from functs import *
from solver import *

SETTINGS = dict()


def parse():
    n_rows, n_cols, n_drones, n_turns, max_payload = _int_list()

    drones = [Drone(i, 0, 0) for i in range(n_drones)]

    n_product_types = int(input())
    products = [Product(i, weight) for i, weight in enumerate(_int_list())]

    n_warehouses = int(input())
    warehouses = []
    for i in range(n_warehouses):
        r, c = _int_list()
        inventory = _int_list()
        warehouses.append(Warehouse(i, r, c, inventory))

    n_orders = int(input())
    orders = []
    for i in range(n_orders):
        r, c = _int_list()
        n_needs = int(input())
        needs = tuple(_frequency_table(n_product_types, _int_list()))
        orders.append(Order(i, r, c, needs))

    order_queue = OrderQueue(warehouses[0], orders)

    SETTINGS.update(n_rows=n_rows, n_cols=n_cols, n_turns=n_turns,
                    max_payload=max_payload, drones=drones, products=products,
                    warehouses=warehouses, orders=orders,
                    order_queue=order_queue)

def _frequency_table(n_product_types, list_):
    counter = Counter(list_)
    return tuple(counter[i] for i in range(n_product_types))



def _int_list():
    return tuple(int(x) for x in input().strip().split())


