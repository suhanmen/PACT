def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        dist1 = planets.index(planet1)
        dist2 = planets.index(planet2)
        if dist1 > dist2:
            dist1, dist2 = dist2, dist1
        return tuple(p for p in planets[dist1+1:dist2] if p != planet1 and p != planet2)
