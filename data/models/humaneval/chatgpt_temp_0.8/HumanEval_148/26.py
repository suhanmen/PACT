def bf(planet1, planet2):
    planet_order = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    p1_idx = planet_order.index(planet1)
    p2_idx = planet_order.index(planet2)
    if p1_idx > p2_idx:
        p1_idx, p2_idx = p2_idx, p1_idx
    return tuple([planet_order[i] for i in range(p1_idx + 1, p2_idx)])
