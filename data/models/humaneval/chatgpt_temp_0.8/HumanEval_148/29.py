def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        index1 = planets.index(planet1)
        index2 = planets.index(planet2)
        if index1 > index2:
            index1, index2 = index2, index1
        return tuple(planet for planet in planets[index1+1:index2] if planet)
    except ValueError:
        return ()
