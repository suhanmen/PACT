python
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        p1_index = planets.index(planet1)
        p2_index = planets.index(planet2)
        if p1_index < p2_index:
            return tuple(sorted(planets[p1_index+1:p2_index], key=lambda x: planets.index(x)))
        else:
            return tuple(sorted(planets[p2_index+1:p1_index], key=lambda x: planets.index(x), reverse=True))
