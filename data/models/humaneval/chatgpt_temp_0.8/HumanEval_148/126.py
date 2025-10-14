def bf(planet1, planet2):
    planet_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    idx1, idx2 = planet_order.index(planet1), planet_order.index(planet2)
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    return tuple([planet_order[i] for i in range(idx1+1, idx2)])
