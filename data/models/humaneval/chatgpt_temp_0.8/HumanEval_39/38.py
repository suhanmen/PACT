def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    fib_nums = [0, 1]
    counter = 2
    while counter <= n:
        next_fib = fib_nums[-1] + fib_nums[-2]
        if is_prime(next_fib):
            fib_nums.append(next_fib)
            counter += 1
        else:
            fib_nums.append(next_fib)
    return fib_nums[-1]
