def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    p1_index = planets.index(planet1)
    p2_index = planets.index(planet2)
    start_index = min(p1_index, p2_index) + 1
    end_index = max(p1_index, p2_index)
    result = tuple([p for p in planets[start_index:end_index] if p != planet1 and p != planet2])
    return result
