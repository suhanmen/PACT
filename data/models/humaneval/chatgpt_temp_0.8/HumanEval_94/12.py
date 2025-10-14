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
    
    largest_prime = None
    for n in lst:
        if is_prime(n):
            if largest_prime is None or n > largest_prime:
                largest_prime = n
    
    if largest_prime is None:
        return 0
    else:
        return sum(int(d) for d in str(largest_prime))
