"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""



def multiple_to_single(int_list):
    return int(''.join(map(str, int_list)))

# Example usage
assert multiple_to_single([11, 33, 50]) == 113350
