# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    num_buckets = 0
    total_water = sum(sum(row) for row in grid)
    while total_water > 0:
        num_buckets += 1
        water_extracted = 0
        for row in grid:
            for i in range(len(row)):
                if row[i] == 1:
                    if water_extracted + 1 <= bucket_capacity:
                        row[i] = 0
                        water_extracted += 1
                        total_water -= 1
                    else:
                        break
            if water_extracted == bucket_capacity:
                break
                
    return num_buckets
