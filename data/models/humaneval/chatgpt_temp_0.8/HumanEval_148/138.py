def bf(planet1, planet2):
    planet_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    elif planet_order.index(planet1) < planet_order.index(planet2):
        return tuple([planet_order[i] for i in range(planet_order.index(planet1)+1, planet_order.index(planet2))])
    else:
        return tuple([planet_order[i] for i in range(planet_order.index(planet2)+1, planet_order.index(planet1))])
