def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()  # Return an empty tuple if either planet is not in the list
    p1_index = planets.index(planet1)
    p2_index = planets.index(planet2)
    if p1_index > p2_index:  # Swap the indices if they are in reverse order
        p1_index, p2_index = p2_index, p1_index
    return tuple([p for p in planets[p1_index+1:p2_index] if p != planet1 and p != planet2])
