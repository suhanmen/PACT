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
        return sum(int(digit) for digit in str(abs(num)))

    nums_with_scores = [(num, digit_sum(num), index) for index, num in enumerate(nums)]
    nums_with_scores.sort(key=lambda x: (x[1], x[2]))
    return [num for num, _, _ in nums_with_scores]
