def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    p1_index = planets.index(planet1)
    p2_index = planets.index(planet2)
    start = min(p1_index, p2_index)
    end = max(p1_index, p2_index)
    result = []
    for i in range(start+1, end):
        result.append(planets[i])
    return tuple(result)
