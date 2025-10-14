def intersection(interval1, interval2):
    # find the intersection between the two intervals
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    # check if the intersection is valid
    if end < start:
        return "NO"

    # calculate the length of the intersection
    length = end - start + 1

    # check if the length is a prime number
    if length < 2:
        return "NO"
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return "NO"

    return "YES"
