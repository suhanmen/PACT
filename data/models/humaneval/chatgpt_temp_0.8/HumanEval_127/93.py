python
def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def intersection(interval1, interval2):
    # check if the intervals intersect
    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return "NO"
    # get the length of the intersection
    intersection_length = min(interval1[1], interval2[1]) - max(interval1[0], interval2[0]) + 1
    # check if the length is prime
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"
