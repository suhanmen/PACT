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
    # Step 1: Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)

    # Step 2: Calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]

    # Step 3: Calculate the average of the absolute differences
    mean_absolute_dev = sum(absolute_diffs) / len(absolute_diffs)

    return mean_absolute_dev
