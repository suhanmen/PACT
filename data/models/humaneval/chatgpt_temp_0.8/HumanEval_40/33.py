def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    if len(l) < 3:
        return False

    # Sort the list for convenience
    l = sorted(l)

    # Loop through the list, fixing the first element
    for i in range(len(l) - 2):
        # Start the two pointers at the beginning and end of the remaining list
        left = i + 1
        right = len(l) - 1

        while left < right:
            # Check if the sum of the three elements is zero
            if l[i] + l[left] + l[right] == 0:
                return True
            # If the sum is too small, move the left pointer to the right
            elif l[i] + l[left] + l[right] < 0:
                left += 1
            # If the sum is too large, move the right pointer to the left
            else:
                right -= 1

    # If no triplets were found, return False
    return False
