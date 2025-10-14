def smallest_change(arr):
    # Initialize pointers for the left and right ends of the array
    left, right = 0, len(arr) - 1

    # Initialize the count of changes to 0
    count = 0

    # Loop through the array until the left and right pointers meet or cross
    while left < right:
        # If the elements at the left and right pointers are the same, move the pointers inward
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            # Otherwise, increment the count of changes and change the smaller of the two elements
            count += 1
            if arr[left] < arr[right]:
                arr[right] = arr[left]
            else:
                arr[left] = arr[right]

    # Return the count of changes
    return count
