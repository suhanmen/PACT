def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        index1 = planets.index(planet1)
        index2 = planets.index(planet2)
        start = min(index1, index2)
        end = max(index1, index2)
        return tuple(sorted(planets[start+1:end], key=planets.index))
