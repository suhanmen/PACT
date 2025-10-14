def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n."""
    result = 0
    for i in range(1, n+1):
        result += i
    return result
