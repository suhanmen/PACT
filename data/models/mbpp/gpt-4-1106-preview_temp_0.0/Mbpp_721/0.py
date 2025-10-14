"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""


import numpy as np

def maxAverageOfPath(matrix):
    N = len(matrix)
    if N == 0:
        return 0

    # Create a DP table to store the sum of costs and number of cells visited
    dp = np.zeros((N, N), dtype=[('sum', 'i4'), ('count', 'i4')])
    dp[0, 0] = (matrix[0][0], 1)

    # Initialize first row and first column
    for i in range(1, N):
        dp[i, 0] = (dp[i-1, 0]['sum'] + matrix[i][0], dp[i-1, 0]['count'] + 1)
        dp[0, i] = (dp[0, i-1]['sum'] + matrix[0][i], dp[0, i-1]['count'] + 1)

    # Fill the DP table
    for i in range(1, N):
        for j in range(1, N):
            if dp[i-1, j]['sum']/dp[i-1, j]['count'] > dp[i, j-1]['sum']/dp[i, j-1]['count']:
                dp[i, j] = (dp[i-1, j]['sum'] + matrix[i][j], dp[i-1, j]['count'] + 1)
            else:
                dp[i, j] = (dp[i, j-1]['sum'] + matrix[i][j], dp[i, j-1]['count'] + 1)

    # The maximum average is in the bottom-right cell
    max_sum, count = dp[N-1, N-1]
    return max_sum / count

# Example usage
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
