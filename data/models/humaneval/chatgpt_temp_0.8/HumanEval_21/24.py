from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1"""
    # find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)
    # calculate the range of the numbers
    range_nums = max_num - min_num
    # apply the linear transformation to each number
    rescaled_nums = [((num - min_num) / range_nums) for num in numbers]
    return rescaled_nums
