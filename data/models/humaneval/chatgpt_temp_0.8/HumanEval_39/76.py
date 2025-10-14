# CANNOT PARSE CODE SNIPPET
def is_prime(num: int) -> bool:
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib_seq = [2, 3]
        while len(fib_seq) < n:
            next_fib = fib_seq[-1] + fib_seq[-2]
            if is_prime(next_fib):
                fib_seq.append(next_fib)
        return fib_seq[-1]
