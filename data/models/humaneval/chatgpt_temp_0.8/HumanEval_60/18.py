def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n."""
    return sum(range(1, n+1))
    
    # Test cases
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(1) == 1
