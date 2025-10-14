def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        count = 2
        prev = 2
        curr = 3
        while count < n:
            next_num = prev + curr
            if is_prime(next_num):
                count += 1
                if count == n:
                    return next_num
            prev = curr
            curr = next_num
