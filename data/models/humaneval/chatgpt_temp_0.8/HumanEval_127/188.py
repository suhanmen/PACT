def is_prime(n):
    """Helper function to determine if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def intersection(interval1, interval2):
    # Get the range of values that intersect between the two intervals
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    # If the range is negative, the intervals don't intersect
    if start > end:
        return "NO"
    # Check if the length of the intersection is prime
    length = end - start + 1
    if is_prime(length):
        return "YES"
    else:
        return "NO"
