def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def digit_sum(num):
        # A helper function to calculate the sum of digits of a number
        return sum(int(d) for d in str(abs(num)))

    # Sort the list based on the digit sum and index
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))
