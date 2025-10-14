python
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet1_index = planets.index(planet1) if planet1 in planets else -1
    planet2_index = planets.index(planet2) if planet2 in planets else -1

    if planet1_index == -1 or planet2_index == -1:
        return ()
    
    start_index = min(planet1_index, planet2_index)
    end_index = max(planet1_index, planet2_index)
    
    return tuple(sorted(planets[start_index+1:end_index], key=lambda x: planets.index(x)))
