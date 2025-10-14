from collections import deque
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    window = deque()
    for i, x in enumerate(numbers):
        while window and numbers[window[-1]] < x:
            window.pop()
        window.append(i)
        result.append(numbers[window[0]])
        if window[0] == i - len(window) + 1:
            window.popleft()
    return result
