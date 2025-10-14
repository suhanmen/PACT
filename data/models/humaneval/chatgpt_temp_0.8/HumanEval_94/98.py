def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    max_prime = None
    for num in lst:
        if is_prime(num):
            if not max_prime or num > max_prime:
                max_prime = num
    
    if max_prime:
        return sum(int(d) for d in str(max_prime))
    else:
        return 0
