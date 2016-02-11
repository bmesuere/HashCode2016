from models import OrderQueue
from main import SETTINGS


def next_avaible_drone_in(position, drones):
    return min(drones, key=drones.ends_in_target(position))



def closest_warehouse_that_fulfills_needs(order, warehouses):
    def distance(warehouse):
        return warehouse.distance(order)
    sorted_warehouses = sorted(warehouses, key=distance)
    for warehouse in sorted_warehouses:
        if fullfills_needs(order, warehouse):
            return warehouse

    # TODO what happens when no warehouse can fulfill this order?
    return None


def fullfills_needs(order, warehouse):
    has_needs = all(stock - need for stock, need in zip(warehouse.stock,
                                                        order.content))
