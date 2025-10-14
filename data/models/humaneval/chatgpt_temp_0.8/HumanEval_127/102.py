def intersection(interval1, interval2):
    # Get the start and end values of the intersection
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    
    # Check if there is no intersection
    if start > end:
        return "NO"
    
    # Compute the length of the intersection
    length = end - start + 1
    
    # Check if the length is a prime number
    if length <= 1:
        return "NO"
    for i in range(2, int(length**0.5)+1):
        if length % i == 0:
            return "NO"
    return "YES"
