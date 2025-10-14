def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planet1_index = planets.index(planet1) if planet1 in planets else None
    planet2_index = planets.index(planet2) if planet2 in planets else None
    if planet1_index is None or planet2_index is None:
        return ()
    left, right = sorted([planet1_index, planet2_index])
    return tuple([planet for i, planet in enumerate(planets) if left < i < right])
