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
    # initialize sum to 0
    sum = 0
    
    # loop through first k elements of arr
    for i in range(k):
        # check if element has at most two digits
        if arr[i] >= 10 and arr[i] <= 99:
            # add element to sum
            sum += arr[i]
    
    # return sum
    return sum
