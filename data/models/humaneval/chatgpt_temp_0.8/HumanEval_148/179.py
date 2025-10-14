def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    planets_between = []
    start_index = planets.index(planet1)
    end_index = planets.index(planet2)
    if start_index > end_index:
        start_index, end_index = end_index, start_index
    for i in range(start_index+1, end_index):
        planets_between.append(planets[i])
    return tuple(planets_between)
