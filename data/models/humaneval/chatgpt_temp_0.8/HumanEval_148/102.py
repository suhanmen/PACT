def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    p1_index = planets.index(planet1)
    p2_index = planets.index(planet2)
    start = p1_index + 1 if p1_index < p2_index else p2_index + 1
    end = p2_index if p1_index < p2_index else p1_index
    return tuple(sorted(planets[start:end], key=lambda x: planets.index(x)))
