def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    planet1_pos = planets.index(planet1)
    planet2_pos = planets.index(planet2)
    if planet1_pos > planet2_pos:
        planet1_pos, planet2_pos = planet2_pos, planet1_pos
    return tuple([p for p in planets[planet1_pos+1:planet2_pos] ])
