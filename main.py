from collections import Counter



def parse():
    n_rows, n_cols, n_drones, n_turns, max_payload = _int_list()
    n_product_types = int(input())
    product_weights = _int_list()
    n_warehouses = int(input())
    warehouses = []
    for i in range(n_warehouses):
        pos = _int_list()
        inventory = _int_list()
        warehouses.append(Warehouse(pos, inventory))
    n_orders = int(input())
    orders = []
    for i in range(n_orders):
        pos = _int_list()
        n_needs = int(input())
        needs = tuple(_frequency_table(n_product_types, _int_list()))
        orders.append(Order(pos, needs))

    return (n_rows, n_cols, n_drones, n_turns, max_payload, product_weights,
            warehouses, orders)


def _frequency_table(n_product_types, list_):
    counter = Counter(list_)
    return tuple(counter[i] for i in range(n_product_types))



def _int_list():
    return tuple(int(x) for x in input().strip().split())


if __name__ == "__main__":
    parse()
