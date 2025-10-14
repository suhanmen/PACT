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
    sums = [(i, sum(int(dig) for dig in str(num))) for i, num in enumerate(nums)]
    sorted_sums = sorted(sums, key=lambda x: (x[1], x[0]))
    return [nums[i] for i, _ in sorted_sums]
