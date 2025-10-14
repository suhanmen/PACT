def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return tuple()
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    if p1 > p2:
        p1, p2 = p2, p1
    return tuple([planets[i] for i in range(p1+1, p2)])
