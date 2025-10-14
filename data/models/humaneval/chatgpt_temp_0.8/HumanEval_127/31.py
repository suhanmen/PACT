import math

def intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if start <= end:
        length = end - start + 1
        if length > 1:
            for i in range(2, int(math.sqrt(length)) + 1):
                if length % i == 0:
                    return "NO"
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
