def make_a_pile(n):
    result = [n]
    for i in range(2, n+1):
        if n % 2 == 0:
            # even case
            next_stones = n + i - 1
        else:
            # odd case
            next_stones = n + i
        result.append(next_stones)
        n = next_stones
    return result
