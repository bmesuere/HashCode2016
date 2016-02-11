
from main import *
from models import *

def solve():
    drones = SETTINGS['drones']
    order_queue = SETTINGS['order_queue']
    warehouses = SETTINGS['warehouses']
    products = SETTINGS['products']

    dronesi = iter(drones)

    current_order = order_queue.pop()
    drone = next(dronesi)
    drone_weight = 0
    drone_carry = []
    for product, count in current_order.products().items():
        while count > 0:
            load_amount = min([count, (SETTINGS['max_payload'] - drone_weight) // product.weight])
            drone.commandqueue.append(Load(
                warehouses[0],
                product,
                load_amount
            ))
            drone_carry.append(product, load_amount)
            drone_weight += load_amount * product.weight
            if load_amount == count:
                for p, c in drone_carry:
                    drone.commandqueue.append(Deliver(current_order, p, c))
                drone = next(dronesi)
                drone_weight = 0
                drone_carry = []
            count -= load_amount

if __name__ == "__main__":
    parse()
    solve()
    print(sum(len(d.commandqueue) for d in drones))
    for d in SETTINGS['drones']:
        for c in d.commandqueue:
            print(d.code, c)
