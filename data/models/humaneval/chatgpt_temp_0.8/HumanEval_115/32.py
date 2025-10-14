# CANNOT PARSE CODE SNIPPET
def max_fill(grid, bucket_capacity):
    import math
    
    # Initialize variables for counting the total number of bucket-lowerings
    lowered_buckets = 0
    total_water = sum(sum(row) for row in grid)
    
    # If there is no water in any of the wells, no bucket-lowerings are needed
    if total_water == 0:
        return 0
    
    # Calculate the number of buckets needed to empty all the wells
    num_buckets = math.ceil(total_water / bucket_capacity)
    
    # Iterate through each level of the wells
    for level in range(len(grid[0])):
        # Initialize a variable to keep track of how much water is in the current bucket
        bucket_contents = 0
        
        # Iterate through each well in the current level
        for well in range(len(grid)):
            # If the current well contains water and the current bucket isn't full, add water to the bucket
            if grid[well][level] == 1 and bucket_contents < bucket_capacity:
                bucket_contents += 1
                
                # If the current bucket is now full, lower it and reset its contents to zero
                if bucket_contents == bucket_capacity:
                    lowered_buckets += 1
                    bucket_contents = 0
                    
        # If there is still water in the current bucket after iterating through all the wells in the current level,
        # lower the bucket
        if bucket_contents > 0:
            lowered_buckets += 1
            
    return lowered_buckets
