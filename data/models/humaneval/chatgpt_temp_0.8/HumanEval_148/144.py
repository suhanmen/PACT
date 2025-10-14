python
def bf(planet1, planet2):
    # Define a list of planets in order from the sun
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    
    # Check if planet1 and planet2 are valid planet names
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    # Find the indices of the planets in the list
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    # Determine the order of the planets
    if index1 < index2:
        start = index1 + 1
        end = index2
    else:
        start = index2 + 1
        end = index1
    
    # Create a list of the planets between the two given planets
    between_planets = [planets[i] for i in range(start, end)]
    
    # Return the between_planets list as a tuple
    return tuple(between_planets)
