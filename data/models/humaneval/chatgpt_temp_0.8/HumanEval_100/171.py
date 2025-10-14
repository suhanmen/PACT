def make_a_pile(n):
    stones = [n]
    level = 2
    while len(stones) < n:
        if n % 2 == 0:
            stones.append(n+level-1)
        else:
            stones.append(n+level)
        level += 1
    return stones
