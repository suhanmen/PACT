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
    # initialize the sum variable
    total_sum = 0

    # iterate through the first k elements of the array
    for i in range(k):
        # check if the element has at most two digits
        if abs(arr[i]) < 100:
            # add the element to the sum if it has at most two digits
            total_sum += arr[i]

    # return the total sum
    return total_sum
