python
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Check if planet1 and planet2 are valid planet names
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    # Get the indices of planet1 and planet2
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    # Sort the indices to get the range of indices between planet1 and planet2
    index_range = sorted([index1, index2])
    
    # Get the planets within the index range
    result = tuple(planets[index_range[0]+1:index_range[1]])
    return result
