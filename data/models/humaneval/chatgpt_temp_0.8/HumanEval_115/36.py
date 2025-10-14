def max_fill(grid, capacity):
    import math

    # count the total number of units of water in the grid
    total_water = 0
    for row in grid:
        total_water += sum(row)

    # if there is no water, no need to lower any buckets
    if total_water == 0:
        return 0

    # calculate the number of times the buckets need to be lowered
    num_buckets = math.ceil(total_water / capacity)
    return num_buckets
