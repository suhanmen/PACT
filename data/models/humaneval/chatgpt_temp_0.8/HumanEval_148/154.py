def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        idx1 = planets.index(planet1)
        idx2 = planets.index(planet2)
        if idx1 < idx2:
            return tuple(sorted(planets[idx1+1:idx2], key=lambda x: planets.index(x)))
        else:
            return tuple(sorted(planets[idx2+1:idx1], key=lambda x: planets.index(x), reverse=True))
