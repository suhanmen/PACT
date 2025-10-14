def intersection(interval1, interval2):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    i1_start, i1_end = interval1
    i2_start, i2_end = interval2
    
    if i1_end < i2_start or i2_end < i1_start:
        return "NO"
    
    intersection_start = max(i1_start, i2_start)
    intersection_end = min(i1_end, i2_end)
    intersection_length = intersection_end - intersection_start + 1
    
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"
