def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 not in planets or planet2 not in planets:
        return ()
    
    index1, index2 = planets.index(planet1), planets.index(planet2)
    start, end = min(index1, index2), max(index1, index2)
    
    return tuple([p for p in planets[start+1:end] if p not in (planet1, planet2)])
