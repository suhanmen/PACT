def prime_fib(n: int):
    def is_prime(num):
        # Returns True if num is prime, False otherwise
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    fib_seq = [0, 1]
    i = 2
    while True:
        next_num = fib_seq[i-1] + fib_seq[i-2]
        if is_prime(next_num):
            if n == 1:
                return next_num
            n -= 1
        fib_seq.append(next_num)
        i += 1
