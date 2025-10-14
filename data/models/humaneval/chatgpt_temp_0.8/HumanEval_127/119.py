def intersection(interval1, interval2):
    # Determine the maximum start value and minimum end value of the two intervals
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    # If the end value is less than the start value, the intervals don't intersect
    if end < start:
        return "NO"

    # Calculate the length of the intersection
    length = end - start + 1

    # Check if the length is a prime number
    if length > 1:
        for i in range(2, int(length ** 0.5) + 1):
            if length % i == 0:
                return "NO"
        return "YES"
    else:
        return "NO"
