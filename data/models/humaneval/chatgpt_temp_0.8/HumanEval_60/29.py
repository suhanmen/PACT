def sum_to_n(n: int):
    """Return the sum of numbers from 1 to n."""
    total = 0
    for i in range(1, n+1):
        total += i
    return total
