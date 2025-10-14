def bf(planet1, planet2):
    # list of planets in order from the sun
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # get the indexes of the two planets
    try:
        index1 = planets.index(planet1)
        index2 = planets.index(planet2)
    except ValueError:
        # if either planet is not in the list, return an empty tuple
        return ()
    
    # sort the indexes to get the range of planets
    start = min(index1, index2)
    end = max(index1, index2)
    
    # create a list of the planets in the range
    range_planets = planets[start+1:end]
    
    # return the range of planets as a tuple
    return tuple(range_planets)
