"""
Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""



def max_of_nth(matrix, n):
    return max(row[n] for row in matrix)

# Example usage
# assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
