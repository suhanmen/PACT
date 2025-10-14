from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Check if any two consecutive numbers are closer than the threshold
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i+1]) < threshold:
            # If two numbers are closer than the threshold, return True
            return True
    
    # If no two numbers are closer than the threshold, return False
    return False
