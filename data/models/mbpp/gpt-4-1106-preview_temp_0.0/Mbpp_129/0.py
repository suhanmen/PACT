"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""


import numpy as np

def magic_square_test(matrix):
    matrix = np.array(matrix)
    if matrix.shape[0] != matrix.shape[1]:
        return False
    n = matrix.shape[0]
    magic_sum = n * (n**2 + 1) // 2
    
    # Check rows and columns
    for i in range(n):
        if sum(matrix[i, :]) != magic_sum or sum(matrix[:, i]) != magic_sum:
            return False
    
    # Check diagonals
    if sum(np.diag(matrix)) != magic_sum or sum(np.diag(np.fliplr(matrix))) != magic_sum:
        return False
    
    return True
