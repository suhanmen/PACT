def pluck(arr):
    if not arr:
        return []
    
    min_even = float('inf')
    min_index = float('inf')
    
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < min_even:
            min_even = arr[i]
            min_index = i
    
    if min_even == float('inf'):
        return []
    
    return [min_even, min_index]
