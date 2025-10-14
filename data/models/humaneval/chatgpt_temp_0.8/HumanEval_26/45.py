from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """Removes duplicates from a list of integers while preserving the order of the remaining elements."""
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
