from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1."""
    
    # Find the minimum and maximum values in the list of numbers
    min_num = min(numbers)
    max_num = max(numbers)
    
    # Calculate the range between the minimum and maximum values
    range_num = max_num - min_num
    
    # Create a new list to store the rescaled values
    rescaled_nums = []
    
    # Loop through each number in the original list
    for num in numbers:
        # Subtract the minimum value from the current number
        num = num - min_num
        
        # Divide the result by the range of values
        num = num / range_num
        
        # Append the rescaled value to the new list
        rescaled_nums.append(num)
    
    return rescaled_nums
