# CANNOT PARSE CODE SNIPPET
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    """
    # Create a new list to hold the interspersed numbers
    interspersed = []
    # Iterate through each number in the input list
    for i in range(len(numbers)):
        # If we're not looking at the last number in the input list
        if i < len(numbers) - 1:
            # Add the current number to the new list
            interspersed.append(numbers[i])
            # Add the delimiter to the new list
            interspersed.append(delimiter)
        # If we are looking at the last number in the input list
        else:
            # Add the current number to the new list, but don't add the delimiter
            interspersed.append(numbers[i])
    # Return the new list with the interspersed numbers
    return interspersed
