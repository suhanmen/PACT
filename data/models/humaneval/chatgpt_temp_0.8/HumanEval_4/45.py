from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    # calculate the sum of the absolute differences between each number and the mean
    sum_abs_diff = sum(abs(number - mean) for number in numbers)
    # divide the sum by the number of numbers to get the mean absolute deviation
    mad = sum_abs_diff / len(numbers)
    return mad
