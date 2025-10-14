python
def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    # Initialize the sum to 0
    total_sum = 0
    
    # Loop from 1 to n (inclusive) and add each number to the sum
    for i in range(1, n+1):
        total_sum += i
    
    # Return the total sum
    return total_sum
