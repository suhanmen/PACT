def make_a_pile(n):
    pile = []
    level = n
    increment = 2 if n % 2 == 0 else 1
    for i in range(n):
        pile.append(level)
        level += increment
        increment += 1
    return pile
