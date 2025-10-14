def bf(planet1, planet2):
    planet_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    index1 = planet_order.index(planet1)
    index2 = planet_order.index(planet2)
    if index1 > index2:
        index1, index2 = index2, index1
    return tuple(planet_order[index1+1:index2])
