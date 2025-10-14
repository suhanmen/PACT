from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()  # sort the list in ascending order
    min_diff = float('inf')  # initialize the minimum difference to infinity
    closest_pair = (0.0, 0.0)  # initialize the closest pair to two zeros
    
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]  # compute the difference between adjacent elements
        
        if diff < min_diff:  # if the difference is smaller than the current minimum
            min_diff = diff  # update the minimum difference
            closest_pair = (numbers[i], numbers[i+1])  # update the closest pair
    
    return closest_pair
