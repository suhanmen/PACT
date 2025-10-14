def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    
def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    
    if start1 > end1 or start2 > end2:
        return "NO"
    
    start = max(start1, start2)
    end = min(end1, end2)
    
    if start > end:
        return "NO"
    
    intersection_length = end - start + 1
    
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"
