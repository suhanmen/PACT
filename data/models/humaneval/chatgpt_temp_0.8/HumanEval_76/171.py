def is_simple_power(x, n):
    if x == 1:   # Special case check for 1
        return True
    i = 1
    while i <= x//n:  # Check if x is divided by n with no remainder
        i *= n
        if i == x:
            return True
    return False      # If no such i exists, then x is not a simple power of n
