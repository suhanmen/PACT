def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    if intersection_start > intersection_end:
        return "NO"
    intersection_length = intersection_end - intersection_start + 1
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"
