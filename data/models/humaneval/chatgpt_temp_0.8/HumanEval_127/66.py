def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """Returns "YES" if the length of intersection is a prime number, "NO" otherwise."""
    start1, end1 = interval1
    start2, end2 = interval2
    
    # check if the intervals intersect
    if end1 < start2 or end2 < start1:
        return "NO"
    
    # determine the length of the intersection
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    intersection_length = intersection_end - intersection_start + 1
    
    # check if the length of intersection is a prime number
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"
