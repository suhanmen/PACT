def max_fill(grid, capacity):
    import math

    num_buckets = 0  # initialize the number of buckets used to 0

    # loop through each well in the grid
    for well in grid:
        # calculate the total amount of water in the well
        well_water = sum(well)

        # calculate the number of buckets needed to empty the well
        num_buckets += math.ceil(well_water / capacity)

    return num_buckets
