def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        start = planets.index(planet1)
        end = planets.index(planet2)
        if start > end:
            start, end = end, start
        result = tuple([p for p in planets[start+1:end] if p])
        return result
