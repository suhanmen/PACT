import math

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    # get the endpoints of the intersection
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    # if the endpoints are not valid, the intervals don't intersect
    if start > end:
        return "NO"
    # check if the length of the intersection is prime
    length = end - start + 1
    if is_prime(length):
        return "YES"
    else:
        return "NO"
