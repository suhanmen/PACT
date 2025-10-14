def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    p1_idx = planets.index(planet1)
    p2_idx = planets.index(planet2)
    
    if p1_idx > p2_idx:
        p1_idx, p2_idx = p2_idx, p1_idx
    
    return tuple([x for x in planets[p1_idx+1:p2_idx]])
