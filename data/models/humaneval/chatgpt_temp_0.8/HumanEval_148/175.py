def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        planets_between = []
        index1 = planets.index(planet1)
        index2 = planets.index(planet2)
        if index1 < index2:
            planets_between = planets[index1+1:index2]
        else:
            planets_between = planets[index2+1:index1]
            planets_between.reverse()
        return tuple(planets_between)
