def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets or planets.index(planet1) == planets.index(planet2):
        return ()
    start = min(planets.index(planet1), planets.index(planet2))
    end = max(planets.index(planet1), planets.index(planet2))
    return tuple(sorted(planets[start+1:end], key=lambda x: planets.index(x)))
