def make_a_pile(n):
    stones_in_level = [n]
    for i in range(n-1):
        if n % 2 == 0:
            stones_in_level.append(stones_in_level[-1]+i+2)
        else:
            stones_in_level.append(stones_in_level[-1]+i+1)
    return stones_in_level
