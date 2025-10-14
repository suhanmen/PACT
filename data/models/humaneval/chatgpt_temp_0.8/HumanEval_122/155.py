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

    # Initialize variable to hold sum
    total = 0

    # Iterate through first k elements of arr
    for num in arr[:k]:
        # Check if number is at most 2 digits
        if num >= 10 and num <= 99:
            # Add to total if it is
            total += num

    # Return the total sum
    return total
