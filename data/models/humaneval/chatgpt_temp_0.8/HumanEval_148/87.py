def bf(planet1, planet2):
    planet_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    
    start = planet_order.index(planet1)
    end = planet_order.index(planet2)
    
    if start > end:
        start, end = end, start
    
    return tuple(planet_order[start+1:end])
