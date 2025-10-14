def move_one_ball(arr):
    # If array is empty, return True
    if not arr:
        return True
    
    n = len(arr)
    # Find the index of the minimum element
    min_index = arr.index(min(arr))
    
    # Check if the array is already sorted
    if sorted(arr) == arr:
        return True
    
    # Shift elements until the minimum element is at index 0
    while min_index != 0:
        arr = arr[-1:] + arr[:-1]
        min_index = (min_index - 1) % n
        
        # If the array is sorted after a shift, return True
        if sorted(arr) == arr:
            return True
    
    # Shift elements until the minimum element is at index 1
    while min_index != 1:
        arr = arr[-1:] + arr[:-1]
        min_index = (min_index - 1) % n
        
        # If the array is sorted after a shift, return True
        if sorted(arr) == arr:
            return True
    
    # It is not possible to get non-decreasing order for the given array
    return False
