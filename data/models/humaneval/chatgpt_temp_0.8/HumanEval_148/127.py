def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    p1_index = planets.index(planet1)
    p2_index = planets.index(planet2)
    min_index = min(p1_index, p2_index)
    max_index = max(p1_index, p2_index)
    return tuple(sorted(planets[min_index+1:max_index], key=lambda x: planets.index(x)))
