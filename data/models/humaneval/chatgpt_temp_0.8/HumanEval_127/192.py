def is_prime(num):
    """Helper function to determine if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    # Check if the intervals intersect
    if end1 < start2 or end2 < start1:
        return "NO"
    # Determine the length of the intersection
    intersection_length = min(end1, end2) - max(start1, start2) + 1
    # Check if the length of the intersection is prime
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"
