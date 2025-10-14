python
def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """Determine if the intersection of two closed intervals is a prime number"""
    start1, end1 = interval1
    start2, end2 = interval2

    # Check if the intervals don't intersect
    if end1 < start2 or end2 < start1:
        return "NO"

    # Calculate the start and end of the intersection
    start = max(start1, start2)
    end = min(end1, end2)

    # Check if the length of the intersection is prime
    if is_prime(end - start + 1):
        return "YES"
    else:
        return "NO"
