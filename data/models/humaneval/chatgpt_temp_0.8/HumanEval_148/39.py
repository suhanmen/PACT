def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    index1 = planets.index(planet1.capitalize()) if planet1.capitalize() in planets else None
    index2 = planets.index(planet2.capitalize()) if planet2.capitalize() in planets else None
    if index1 is None or index2 is None:
        return ()
    start = min(index1, index2)
    end = max(index1, index2)
    return tuple(sorted(planets[start+1:end], key=lambda p: planets.index(p)))
