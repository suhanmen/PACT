def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    first_index = planets.index(planet1)
    second_index = planets.index(planet2)
    start = min(first_index, second_index)
    end = max(first_index, second_index)
    result = tuple([planet for planet in planets[start+1:end] if planet != planet1 and planet != planet2])
    return result
