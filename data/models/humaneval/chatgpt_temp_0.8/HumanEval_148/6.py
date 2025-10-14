def bf(planet1, planet2):
    # A dictionary to map planet names to their respective order from the Sun
    planet_order = {"Mercury": 1, "Venus": 2, "Earth": 3, "Mars": 4, "Jupiter": 5, "Saturn": 6, "Uranus": 7, "Neptune": 8}
    
    # Check if planet1 and planet2 are valid planet names
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    
    # Find the orbit order of planet1 and planet2
    orbit1 = planet_order[planet1]
    orbit2 = planet_order[planet2]
    
    # Swap orbit1 and orbit2 if orbit1 is greater than orbit2
    if orbit1 > orbit2:
        orbit1, orbit2 = orbit2, orbit1
    
    # A list to store the planets whose orbits are located between planet1 and planet2
    planets = []
    
    # Iterate through the planet_order dictionary and add planets to the list if their orbit order is between orbit1 and orbit2
    for planet, orbit in planet_order.items():
        if orbit1 < orbit < orbit2:
            planets.append(planet)
    
    # Sort the planets by the
