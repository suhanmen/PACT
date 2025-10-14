def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets or planets.index(planet1) == planets.index(planet2):
        return ()
    elif planets.index(planet1) > planets.index(planet2):
        planet1, planet2 = planet2, planet1
    return tuple([planet for planet in planets if planets.index(planet1) < planets.index(planet) < planets.index(planet2)])
