def bf(planet1, planet2):
    planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planet_names or planet2 not in planet_names:
        return ()
    else:
        index1 = planet_names.index(planet1)
        index2 = planet_names.index(planet2)
        if index1 < index2:
            return tuple(sorted(planet_names[index1+1:index2], key=lambda x: planet_names.index(x)))
        else:
            return tuple(sorted(planet_names[index2+1:index1], key=lambda x: planet_names.index(x), reverse=True))
