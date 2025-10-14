def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
    start1, end1 = interval1
    start2, end2 = interval2
    
    # Find the start and end of the intersection
    start_inter = max(start1, start2)
    end_inter = min(end1, end2)
    
    # Check if there is an intersection
    if end_inter < start_inter:
        return "NO"
    
    # Compute the length of the intersection
    length = end_inter - start_inter + 1
    
    # Check if the length is prime
    if length < 2:
        return "NO"
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return "NO"
    
    return "YES"
