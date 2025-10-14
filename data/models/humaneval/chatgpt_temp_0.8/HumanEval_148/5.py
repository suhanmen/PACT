def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    try:
        planet1_idx = planets.index(planet1)
        planet2_idx = planets.index(planet2)
    except ValueError:
        return ()
    
    if planet1_idx > planet2_idx:
        planet1_idx, planet2_idx = planet2_idx, planet1_idx
        
    return tuple([planet for planet in planets[planet1_idx+1:planet2_idx] if planet])
