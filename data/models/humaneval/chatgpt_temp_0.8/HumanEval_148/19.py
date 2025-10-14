def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        p1_index = planets.index(planet1)
        p2_index = planets.index(planet2)
        if p1_index > p2_index:
            p1_index, p2_index = p2_index, p1_index
        return tuple([planet for planet in planets if p1_index < planets.index(planet) < p2_index])
