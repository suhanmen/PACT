def is_prime(num: int) -> bool:
        """
        Helper function that checks if a number is a prime number
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    fib = [0, 1]
    i = 2
    while True:
        next_fib = fib[i-1] + fib[i-2]
        if is_prime(next_fib):
            n -= 1
            if n == 0:
                return next_fib
        fib.append(next_fib)
        i += 1
