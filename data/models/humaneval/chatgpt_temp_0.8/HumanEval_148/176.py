def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    orbit1 = planets.index(planet1)
    orbit2 = planets.index(planet2)
    if orbit1 > orbit2:
        orbit1, orbit2 = orbit2, orbit1
    return tuple(sorted(planets[orbit1+1:orbit2], key=lambda x: planets.index(x)))
