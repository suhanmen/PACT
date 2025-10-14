def intersection(interval1, interval2):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    start1, end1 = interval1
    start2, end2 = interval2
    
    # Find the overlap, if any
    overlap_start = max(start1, start2)
    overlap_end = min(end1, end2)
    
    # If no overlap, return "NO"
    if overlap_start > overlap_end:
        return "NO"
    
    # Compute the length of the overlap and check if it's prime
    overlap_length = overlap_end - overlap_start + 1
    if is_prime(overlap_length):
        return "YES"
    else:
        return "NO"
