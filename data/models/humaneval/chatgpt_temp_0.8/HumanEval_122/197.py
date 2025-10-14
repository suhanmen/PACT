def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # Initialize sum variable
    sum = 0
    
    # Loop through first k elements of arr
    for i in range(k):
        # Check if element has at most two digits
        if arr[i] < 100:
            # Add element to sum
            sum += arr[i]
    
    # Return sum of elements with at most two digits
    return sum
