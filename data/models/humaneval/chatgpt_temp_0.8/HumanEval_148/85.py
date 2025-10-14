def bf(planet1, planet2):
    planets = {"Mercury": 1, "Venus": 2, "Earth": 3, "Mars": 4, "Jupiter": 5, "Saturn": 6, "Uranus": 7, "Neptune": 8}
    if planet1 not in planets or planet2 not in planets:
        return ()
    min_planet = min(planets[planet1], planets[planet2])
    max_planet = max(planets[planet1], planets[planet2])
    result = tuple([planet for planet, order in planets.items() if min_planet < order < max_planet])
    return result
