"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""


import math

def find_solution(a, b, n):
    # Check if there are any solutions
    gcd = math.gcd(a, b)
    if n % gcd != 0:
        return None
    
    # Extended Euclidean Algorithm to find one solution
    def extended_gcd(aa, bb):
        if aa == 0:
            return (bb, 0, 1)
        else:
            g, x, y = extended_gcd(bb % aa, aa)
            return (g, y - (bb // aa) * x, x)
    
    g, x, y = extended_gcd(a, b)
    # Scale the solution to the specific value of n
    x *= n // g
    y *= n // g
    
    # Return the solution as a tuple
    return (x, y)

# Example usage
# solution = find_solution(2, 3, 7)
# if solution:
#     print(f'Solution found: x = {solution[0]}, y = {solution[1]}')
# else:
#     print('No solution exists')
