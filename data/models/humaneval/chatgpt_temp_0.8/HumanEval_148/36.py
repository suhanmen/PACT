def bf(planet1, planet2):
    planets_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets_order or planet2 not in planets_order:
        return ()
    else:
        start = planets_order.index(planet1)
        end = planets_order.index(planet2)
        if start > end:
            start, end = end, start
        return tuple([planet for planet in planets_order[start+1:end]])
