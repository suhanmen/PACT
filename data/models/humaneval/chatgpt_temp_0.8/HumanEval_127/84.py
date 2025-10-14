def intersection(interval1, interval2):
    # Find the intersection of the two intervals
    intersection_start = max(interval1[0], interval2[0])
    intersection_end = min(interval1[1], interval2[1])
    
    # If there is no intersection, return "NO"
    if intersection_start > intersection_end:
        return "NO"
    
    # Calculate the length of the intersection
    intersection_length = intersection_end - intersection_start + 1
    
    # Check if the length of the intersection is a prime number
    if intersection_length < 2:
        return "NO"
    for i in range(2, int(intersection_length**0.5) + 1):
        if intersection_length % i == 0:
            return "NO"
    
    # If the length of the intersection is a prime number, return "YES"
    return "YES"
