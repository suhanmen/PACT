def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    idx1, idx2 = planets.index(planet1), planets.index(planet2)
    start_idx, end_idx = min(idx1, idx2), max(idx1, idx2)
    result = []
    for i in range(start_idx+1, end_idx):
        result.append(planets[i])
    return tuple(result)
