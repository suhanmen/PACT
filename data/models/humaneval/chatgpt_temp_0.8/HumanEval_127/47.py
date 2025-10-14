def intersection(interval1, interval2):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    start1, end1 = interval1
    start2, end2 = interval2
    
    # check for overlap
    if end1 < start2 or end2 < start1:
        return "NO"
    
    # compute intersection length
    start = max(start1, start2)
    end = min(end1, end2)
    intersection_length = end - start + 1
    
    # check if intersection length is prime
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"
