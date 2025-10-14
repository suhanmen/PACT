def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    a,b = interval1
    c,d = interval2
    if b<a:
        a,b = b,a
    if d<c:
        c,d = d,c
    if b<c or d<a:
        return "NO"
    length = min(b,d)-max(a,c)+1
    if is_prime(length):
        return "YES"
    else:
        return "NO"
