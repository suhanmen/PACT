from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest = None
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if closest is None or abs(numbers[i] - numbers[j]) < abs(closest[0] - closest[1]):
                closest = (numbers[i], numbers[j])
    return tuple(sorted(closest))
