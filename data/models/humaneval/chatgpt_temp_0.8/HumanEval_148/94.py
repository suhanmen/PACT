def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    sorted_planets = planets[min(p1, p2)+1:max(p1, p2)]
    return tuple(sorted_planets)
