def bf(planet1, planet2):
    planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        idx1 = planets.index(planet1)
        idx2 = planets.index(planet2)
        start = min(idx1, idx2)
        end = max(idx1, idx2)
        result = tuple([planet for planet in planets[start+1:end] if planet])
        return result
