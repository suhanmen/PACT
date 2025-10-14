python
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    if end1 < start2 or end2 < start1:
        return "NO"  # No intersection
    else:
        intersection_start = max(start1, start2)
        intersection_end = min(end1, end2)
        intersection_length = intersection_end - intersection_start + 1
        if is_prime(intersection_length):
            return "YES"
        else:
            return "NO"
