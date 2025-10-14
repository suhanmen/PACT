def intersection(interval1, interval2):
    # Determine the start and end points of the intersection
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    
    # If the start point is greater than the end point, the intervals don't intersect
    if start > end:
        return "NO"
    
    # Determine the length of the intersection
    length = end - start + 1
    
    # Check if the length is a prime number
    if length < 2:
        return "NO"
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return "NO"
    
    return "YES"
