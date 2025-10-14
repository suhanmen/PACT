python
def max_fill(grid, capacity):
    import math
    
    count = 0
    
    for row in grid:
        # Calculate the total amount of water in the current row
        row_sum = sum(row)
        
        # Calculate the number of times we need to lower the bucket for this row
        row_count = math.ceil(row_sum/capacity)
        
        # Add the row count to the total count
        count += row_count
    
    return count
