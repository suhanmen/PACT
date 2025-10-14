def prime_fib(n: int):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    fib = [0, 1]
    index = 2
    while True:
        # Calculate next Fibonacci number
        next_fib = fib[index-1] + fib[index-2]
        if is_prime(next_fib):
            n -= 1
            if n == 0:
                return next_fib
        # Append next Fibonacci number to list
        fib.append(next_fib)
        index += 1
