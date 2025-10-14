def move_one_ball(arr):
    if not arr:  # If the array is empty, return True
        return True
    
    n = len(arr)
    index = 0
    
    for i in range(1, n):  # Loop through the array to find the smallest element
        if arr[i] < arr[index]:
            index = i
    
    # Check if the smallest element is already at the beginning of the array
    if index == 0:
        return True
    
    # Check if the remaining elements are sorted in non-decreasing order
    for i in range(n-1):
        if arr[(index+i)%n] > arr[(index+i+1)%n]:
            return False
    
    return True
