def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    if planet1 not in planets or planet2 not in planets:
        return ()

    i1, i2 = planets.index(planet1), planets.index(planet2)
    if i1 > i2:
        i1, i2 = i2, i1

    return tuple(p for p in planets[i1+1:i2] if p)
