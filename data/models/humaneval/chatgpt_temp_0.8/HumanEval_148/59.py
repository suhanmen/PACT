def bf(planet1, planet2):
    # Define a dictionary to map each planet to its distance from the sun
    planet_distances = {"Mercury": 1, "Venus": 2, "Earth": 3, "Mars": 4, 
                        "Jupiter": 5, "Saturn": 6, "Uranus": 7, "Neptune": 8}
    
    # Check if planet1 and planet2 are valid planet names
    if planet1 not in planet_distances or planet2 not in planet_distances:
        return ()
    
    # Get the distances of planet1 and planet2 from the sun
    p1_distance = planet_distances[planet1]
    p2_distance = planet_distances[planet2]
    
    # Determine the range of planet distances to include
    if p1_distance < p2_distance:
        start = p1_distance + 1
        end = p2_distance
    else:
        start = p2_distance + 1
        end = p1_distance
    
    # Create a list of planet names within the specified range
    planets_within_range = []
    for planet, distance in planet_distances.items():
        if start <= distance <= end:
            planets_within_range.append(planet)
    
