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
    if not nums:
        return []
    num_dict = {}
    for num in nums:
        digit_sum = sum(int(digit) for digit in str(abs(num)))
        if digit_sum in num_dict:
            num_dict[digit_sum].append(num)
        else:
            num_dict[digit_sum] = [num]
    result = []
    for key in sorted(num_dict.keys()):
        result.extend(sorted(num_dict[key], key=lambda x: nums.index(x)))
    return result
