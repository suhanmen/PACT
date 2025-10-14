# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math

    # Helper function to get the total number of units of water in the grid
    def get_total_water():
        total_water = 0
        for row in grid:
            total_water += sum(row)
        return total_water

    # Check if the grid is already empty
    if get_total_water() == 0:
        return 0

    # Calculate the number of buckets needed to empty the grid
    num_buckets = math.ceil(get_total_water() / bucket_capacity)

    # Calculate the number of times the buckets need to be lowered
    num_lowerings = 0
    while num_buckets > 0:
        # Lower the buckets and empty the wells
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    num_buckets -= 1
                    if num_buckets == 0:
                        break
            if num_buckets == 0:
                break
        num_lowerings += 1

    return num_lowerings
