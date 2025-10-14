def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    elif planets.index(planet1) > planets.index(planet2):
        planet1, planet2 = planet2, planet1
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    between = planets[index1+1:index2]
    return tuple(between)
