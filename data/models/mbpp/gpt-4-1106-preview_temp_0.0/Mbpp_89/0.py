"""
Write a function to find the closest smaller number than n.
assert closest_num(11) == 10
"""



def closest_num(n):
    # Assuming n is an integer
    return n - 1 if n > 0 else None

# Example usage
# closest_num(11) will return 10
