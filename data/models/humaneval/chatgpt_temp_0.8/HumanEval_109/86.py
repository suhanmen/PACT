def move_one_ball(arr):
    # If the given list is empty, return True
    if not arr:
        return True
    
    # Find the index of the minimum element in the array
    min_index = arr.index(min(arr))
    
    # Perform right shift operation to move the minimum element to the first position
    arr = arr[min_index:] + arr[:min_index]
    
    # Check if the array is sorted in non-decreasing order
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
        
    return True
