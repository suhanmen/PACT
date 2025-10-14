def max_fill(grid, capacity):
    import math
    wells = sum(sum(row) for row in grid)
    return math.ceil(wells/capacity)
