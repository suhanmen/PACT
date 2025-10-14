"""
Write a function to find the n'th star number.
assert find_star_num(3) == 37
"""



def find_star_num(n):
    if n < 1:
        return None
    return 6 * (n - 1) * n + 1

# Example usage
# find_star_num(3) should return 37
