def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    prime_lst = []
    for num in lst:
        if is_prime(num):
            prime_lst.append(num)
    if len(prime_lst) == 0:
        return 0
    max_prime = max(prime_lst)
    digits_sum = sum(int(digit) for digit in str(max_prime))
    return digits_sum
    """
