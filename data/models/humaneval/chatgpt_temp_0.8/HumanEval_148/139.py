def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    result = []
    if planet1 not in planets or planet2 not in planets:
        return tuple(result)
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    index_start = min(index1, index2) + 1
    index_end = max(index1, index2)
    for i in range(index_start, index_end):
        result.append(planets[i])
    return tuple(result)
