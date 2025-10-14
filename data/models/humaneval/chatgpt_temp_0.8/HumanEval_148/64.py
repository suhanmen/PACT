def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ()
    planets_between = []
    for planet in planets:
        if planet == planet1:
            start_index = planets.index(planet)
        elif planet == planet2:
            end_index = planets.index(planet)
            break
    if start_index > end_index:
        start_index, end_index = end_index, start_index
    planets_between = planets[start_index+1:end_index]
    return tuple(planets_between)
