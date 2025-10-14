def bf(planet1, planet2):
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]
    if planet1 not in planets or planet2 not in planets:
        return ()
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    if idx1 == idx2:
        return ()
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    return tuple(p for p in planets[idx1+1:idx2] if p != planet1 and p != planet2)
