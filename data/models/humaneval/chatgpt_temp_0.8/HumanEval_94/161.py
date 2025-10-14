def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.
    """
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    max_prime = None
    for num in lst:
        if is_prime(num):
            if max_prime is None or num > max_prime:
                max_prime = num
    
    if max_prime is not None:
        return sum(int(digit) for digit in str(max_prime))
    else:
        return 0
