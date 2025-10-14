def is_prime(n):
    """Helper function to check if a given number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    start = max(start1, start2)
    end = min(end1, end2)
    if start > end:
        return "NO"
    length = end - start + 1
    return "YES" if is_prime(length) else "NO"
