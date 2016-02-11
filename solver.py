
from main import *
from models import *
from sys import stderr

def solve():
    drones = SETTINGS['drones']
    order_queue = SETTINGS['order_queue']
    warehouses = SETTINGS['warehouses']
    products = SETTINGS['products']

    dronesi = iter(drones)

    while True:
        sums = max(d.ends_in()[0] for d in drones)
        print(sums, file=stderr)
        if SETTINGS['n_turns'] < sums:
            break
        current_order = order_queue.pop()

        drones_used_for_order = []
        drones_used_for_order.append(next_avaible_drone_in(warehouses[0], drones))
        for product, count in current_order.products():
            for drone in drones_used_for_order:
                load_amount = min([count, (SETTINGS['max_payload'] - drone.load_weight()) // product.weight])
                drone.add_load(product.code, load_amount)
                warehouses[0].stock[product.code] -= load_amount
                count -= load_amount
                if load_amount == 0:
                    break
            else:
                while count > 0:
                    drone = next_avaible_drone_in(warehouses[0], drones)
                    drones_used_for_order.append(drone)
                    load_amount = min([count, (SETTINGS['max_payload'] - drone_weight) // product.weight])
                    drone.add_load(product.code, load_amount)
                    warehouses[0].stock[product.code] -= load_amount
                    count -= load_amount
        for drone in drones_used_for_order:
            for p, c in drone.load.items():
                drone.deliver(current_order, p, c)

if __name__ == "__main__":
    parse()
    try:
        solve()
    except IndexError:
        pass
    except KeyboardInterrupt:
        pass
    print(sum(len(d.commandqueue) for d in SETTINGS['drones']))
    for d in SETTINGS['drones']:
        for c in d.commandqueue:
            print(d.code, c)
