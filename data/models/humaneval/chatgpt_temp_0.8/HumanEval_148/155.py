def bf(planet1, planet2):
    all_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in all_planets or planet2 not in all_planets:
        return ()
    idx1 = all_planets.index(planet1)
    idx2 = all_planets.index(planet2)
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    return tuple(sorted(all_planets[idx1+1:idx2], key=lambda x: all_planets.index(x)))
