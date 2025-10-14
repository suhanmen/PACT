def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    if start1 > end1 or start2 > end2:
        return "NO"
    intersect_start = max(start1, start2)
    intersect_end = min(end1, end2)
    if intersect_start > intersect_end:
        return "NO"
    intersect_length = intersect_end - intersect_start + 1
    if is_prime(intersect_length):
        return "YES"
    else:
        return "NO"
