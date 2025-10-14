# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math

    # Calculate the total amount of water in the grid
    total_water = sum([sum(row) for row in grid])

    # If there's no water, return 0
    if total_water == 0:
        return 0

    # Calculate the number of times we need to empty the buckets
    num_buckets = math.ceil(total_water / bucket_capacity)

    # Return the result
    return num_buckets
