def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    start = min(idx1, idx2) + 1
    end = max(idx1, idx2)
    return tuple(sorted(planets[start:end]))
