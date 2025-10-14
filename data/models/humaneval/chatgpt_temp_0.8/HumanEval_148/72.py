def bf(planet1, planet2):
    planets = {
        "Mercury": 1,
        "Venus": 2,
        "Earth": 3,
        "Mars": 4,
        "Jupiter": 5,
        "Saturn": 6,
        "Uranus": 7,
        "Neptune": 8
    }
    if planet1 not in planets or planet2 not in planets:
        return ()
    p1 = planets[planet1]
    p2 = planets[planet2]
    if p1 > p2:
        p1, p2 = p2, p1
    result = []
    for planet, orbit in planets.items():
        if p1 < orbit < p2:
            result.append(planet)
    return tuple(result)
