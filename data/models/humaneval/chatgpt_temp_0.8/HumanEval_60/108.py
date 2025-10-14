python
def sum_to_n(n: int):
    """Sums numbers from 1 to n."""
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
