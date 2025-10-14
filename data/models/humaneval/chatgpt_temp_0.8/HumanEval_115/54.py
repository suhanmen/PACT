def max_fill(grid, capacity):
    import math
    total_water = sum(sum(row) for row in grid)
    return math.ceil(total_water/capacity)
