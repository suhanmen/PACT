def get_row(lst, x):
    # Initialize an empty result list
    result = []
    
    # Loop through each row in the list
    for i, row in enumerate(lst):
        # If the integer x is in the row
        if x in row:
            # Loop through each index in the row
            for j, num in enumerate(row):
                # If the number is x, append the coordinate to the result list
                if num == x:
                    result.append((i, j))
    
    # Sort the result list by rows in ascending order
    result.sort(key=lambda coord: coord[0])
    
    # Sort the result list of each row by columns in descending order
    for i in range(len(result)):
        row = lst[result[i][0]]
        row_coords = [coord for coord in result if coord[0] == result[i][0]]
        row_coords.sort(key=lambda coord: coord[1], reverse=True)
        result[i:i+len(row_coords)] = row_coords
    
    return result
