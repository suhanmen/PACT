def largest_divisor(n: int) -> int:
    # start from n-1 and iterate down to 1
    for i in range(n-1, 0, -1):
        # if i divides n evenly, return i
        if n % i == 0:
            return i
    # if no divisor found, return None or raise an exception
    return None
