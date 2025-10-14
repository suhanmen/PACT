# CANNOT PARSE CODE SNIPPET
def prime_fib(n: int) -> int:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if n < 1:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 2
    if n == 2:
        return 3

    prev = 2
    curr = 3
    count = 2
    while True:
        next_num = prev + curr
        if is_prime(next_num):
            count += 1
            if count == n:
                return next_num
        prev, curr = curr, next_num
