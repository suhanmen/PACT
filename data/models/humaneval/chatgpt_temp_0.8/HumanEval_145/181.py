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

    def get_sum_of_digits(num):
        # A helper function to get the sum of the digits in a number.
        # If the number is negative, we ignore the negative sign for digit sum purposes.
        if num < 0:
            num = -num
        return sum(int(digit) for digit in str(num))

    # Use the get_sum_of_digits helper function to sort the list of numbers by their digit sum.
    sorted_nums = sorted(nums, key=lambda num: (get_sum_of_digits(num), nums.index(num)))

    return sorted_nums
