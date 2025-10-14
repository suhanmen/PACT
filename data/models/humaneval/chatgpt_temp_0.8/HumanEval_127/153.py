def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if end < start:
        return "NO"
    elif end == start:
        return "YES" if is_prime(end) else "NO"
    else:
        length = end - start
        return "YES" if is_prime(length) else "NO"
