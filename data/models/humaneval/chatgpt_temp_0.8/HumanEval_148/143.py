def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    planet1_idx = planets.index(planet1)
    planet2_idx = planets.index(planet2)
    if planet1_idx > planet2_idx:
        planet1_idx, planet2_idx = planet2_idx, planet1_idx
    return tuple([x for x in planets[planet1_idx+1:planet2_idx] if x])
