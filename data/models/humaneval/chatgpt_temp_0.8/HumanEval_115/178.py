# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    total_water = sum(sum(row) for row in grid)
    if total_water == 0:
        return 0
    else:
        return math.ceil(total_water / bucket_capacity)
