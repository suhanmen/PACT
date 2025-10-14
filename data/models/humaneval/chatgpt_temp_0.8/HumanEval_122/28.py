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
    sum = 0 # initialize variable to store sum of elements
    for i in range(k): # loop through first k elements of array
        if arr[i] >= 10 and arr[i] < 100: # check if element has at most two digits
            sum += arr[i] # add to sum if element has at most two digits
    return sum # return sum of elements with at most two digits
