def is_prime(n):
    """helper function to check if number n is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    if end1 < start2 or end2 < start1:  # no intersection
        return "NO"
    start = max(start1, start2)
    end = min(end1, end2)
    length = end - start + 1
    if is_prime(length):
        return "YES"
    else:
        return "NO"
