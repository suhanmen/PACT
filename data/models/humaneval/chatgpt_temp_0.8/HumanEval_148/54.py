def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)
    start = min(planet1_index, planet2_index)
    end = max(planet1_index, planet2_index)
    return tuple([planet for planet in planets[start+1:end]])
