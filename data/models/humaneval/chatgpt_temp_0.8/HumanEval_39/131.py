def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**(0.5))+1):
            if num % i == 0:
                return False
        return True
    
    fib_nums = [0, 1]
    while True:
        curr_fib = fib_nums[-1] + fib_nums[-2]
        if is_prime(curr_fib):
            if len(fib_nums) == n+1:
                return curr_fib
            else:
                fib_nums.append(curr_fib)
        else:
            fib_nums.append(curr_fib)
