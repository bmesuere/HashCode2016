
from main import *
from models import *

def solve():
    drones = SETTINGS['drones']
    order_queue = SETTINGS['order_queue']
    warehouses = SETTINGS['warehouses']
    products = SETTINGS['products']
    drones[0].commandqueue.append(Wait(3))
    drones[0].commandqueue.append(Deliver(order_queue.pop()[1],
        products[0], 3))
    return drones

if __name__ == "__main__":
    parse()
    drones = solve()
    print(sum(len(d.commandqueue) for d in drones))
    for d in drones:
        for c in d.commandqueue:
            print(d.code, c)
