def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    start = planets.index(planet1)
    end = planets.index(planet2)
    if start > end:
        start, end = end, start
    return tuple([p for p in planets[start+1:end] if p != planet1 and p != planet2])
