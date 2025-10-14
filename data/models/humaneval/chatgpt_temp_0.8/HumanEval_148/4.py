def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet_indexes = [planets.index(planet1), planets.index(planet2)]
    if -1 in planet_indexes or planet_indexes[0] == planet_indexes[1]:
        return ()
    start = min(planet_indexes)
    end = max(planet_indexes)
    return tuple(sorted(planets[start+1:end], key=lambda x: planets.index(x)))
