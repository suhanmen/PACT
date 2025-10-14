python
def intersection(interval1, interval2):
    a, b = interval1
    c, d = interval2

    if max(a, c) <= min(b, d): # check if the intervals intersect
        intersection_length = min(b, d) - max(a, c) + 1
        if intersection_length <= 1: # if intersection is less than or equal to 1, return "NO"
            return "NO"
        else:
            for i in range(2, int(intersection_length ** 0.5) + 1): # check if intersection length is prime
                if intersection_length % i == 0:
                    return "NO"
            return "YES"
    else:
        return "NO"
