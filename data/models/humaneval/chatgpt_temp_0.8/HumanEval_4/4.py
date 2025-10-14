from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean | """
    x_mean = sum(numbers) / len(numbers)
    deviations = [abs(x - x_mean) for x in numbers]
    return sum(deviations) / len(deviations)

