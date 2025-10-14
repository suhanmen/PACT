# CANNOT PARSE
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if start > end:
        return "NO"

    length = end - start

    if is_prime(length):
        return "YES"
    else:
        return "NO"

# Test cases
print(intersection((1, 2), (2, 3))) #==> "NO"
print(intersection((-1, 1), (0, 4))) #==> "NO"
print(intersection((-3, -1), (-5, 5))) #==> "YES"