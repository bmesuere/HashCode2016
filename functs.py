
def next_avaible_drone_in(position, drones):
    return min(drones, key=drones.ends_in_target(position))

