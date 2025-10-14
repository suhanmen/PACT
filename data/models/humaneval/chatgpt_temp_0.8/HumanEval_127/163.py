def intersection(interval1, interval2):
    # Find the intersection interval between the two input intervals
    intersection_start = max(interval1[0], interval2[0])
    intersection_end = min(interval1[1], interval2[1])
    intersection_length = intersection_end - intersection_start + 1

    # Check if the intersection interval is valid and has a prime length
    if intersection_length > 0 and is_prime(intersection_length):
        return "YES"
    else:
        return "NO"

