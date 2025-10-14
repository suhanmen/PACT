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

    # Initialize a variable to store the sum of elements with at most two digits
    sum_two_digits = 0
    
    # Iterate through the first k elements of the array
    for i in range(k):
        # Check if the element has at most two digits
        if arr[i] >= 10 and arr[i] <= 99:
            # Add the element to the sum of two-digit elements
            sum_two_digits += arr[i]
    
    # Return the sum of two-digit elements
    return sum_two_digits
