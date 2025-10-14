def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    max_prime = -1
    for num in lst:
        if is_prime(num) and num > max_prime:
            max_prime = num

    if max_prime == -1:
        return 0

    return sum(int(digit) for digit in str(max_prime))
