def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        index1 = planets.index(planet1)
        index2 = planets.index(planet2)
        start = min(index1, index2)
        end = max(index1, index2)
        return tuple(sorted(planets[start+1:end], key=lambda x: planets.index(x)))
    except ValueError:
        return ()
