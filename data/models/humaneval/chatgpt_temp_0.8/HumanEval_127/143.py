def intersection(interval1, interval2):
    # find the maximum start and minimum end of the two intervals
    max_start = max(interval1[0], interval2[0])
    min_end = min(interval1[1], interval2[1])

    # check if the two intervals don't intersect
    if max_start > min_end:
        return "NO"

    # find the length of the intersection
    length = min_end - max_start + 1

    # check if the length is a prime number
    if length <= 1:
        return "NO"
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return "NO"

    return "YES"
