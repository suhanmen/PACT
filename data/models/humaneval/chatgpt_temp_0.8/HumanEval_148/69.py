def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    planet1_idx = planets.index(planet1)
    planet2_idx = planets.index(planet2)
    start = min(planet1_idx, planet2_idx)
    end = max(planet1_idx, planet2_idx)
    return tuple(sorted(planets[start+1:end], key=lambda x: planets.index(x)))
