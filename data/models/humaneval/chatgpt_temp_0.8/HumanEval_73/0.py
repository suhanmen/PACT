def smallest_change(arr):
    if arr == arr[::-1]:
        # Base case: array is already a palindrome
        return 0
    
    # Recursive case: try changing either the first or last element
    if arr[0] == arr[-1]:
        # If the first and last element are the same, check the rest of the array
        return smallest_change(arr[1:-1])
    else:
        # Otherwise, try changing the first element or the last element
        return 1 + min(smallest_change(arr[1:]), smallest_change(arr[:-1]))
