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
    n = len(numbers)
    if n < 2:
        raise ValueError("MAD requires at least two data points")
    
    mean = sum(numbers) / n
    absolute_deviations = [abs(x - mean) for x in numbers]
    
    return sum(absolute_deviations) / n
