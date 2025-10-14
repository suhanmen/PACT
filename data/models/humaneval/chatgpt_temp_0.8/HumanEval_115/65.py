# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math

    def get_num_buckets(well, bucket_capacity):
        return math.ceil(sum(well)/bucket_capacity)

    def get_num_lowerings(grid_row, bucket_capacity):
        num_buckets = get_num_buckets(grid_row, bucket_capacity)
        num_lowerings = 0
        for i in range(0, len(grid_row), bucket_capacity):
            num_lowerings += 1
            for j in range(i, min(i+bucket_capacity, len(grid_row))):
                if grid_row[j] == 1:
                    num_buckets -= 1
            if num_buckets == 0:
                break
        return num_lowerings

    total_lowerings = 0
    for row in grid:
        total_lowerings += get_num_lowerings(row, bucket_capacity)
    return total_lowerings
