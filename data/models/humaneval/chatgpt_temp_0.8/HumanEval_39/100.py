# CANNOT PARSE CODE SNIPPET
def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        i = 3
        fib_n_minus2 = 2
        fib_n_minus1 = 3
        while i <= n:
            fib_n = fib_n_minus1 + fib_n_minus2
            if is_prime(fib_n):
                if i == n:
                    return fib_n
                i += 1
            fib_n_minus2 = fib_n_minus1
            fib_n_minus1 = fib_n
            i += 1
