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
    nums_with_digits_sum = []
    for num in nums:
        digits_sum = sum(int(digit) for digit in str(abs(num)))
        nums_with_digits_sum.append((num, digits_sum))
    sorted_nums = sorted(nums_with_digits_sum, key=lambda x: (x[1], nums.index(x[0])))
    return [num[0] for num in sorted_nums]
