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
        previous = 2
        current = 3
        for i in range(3, n+1):
            next_num = previous + current
            previous = current
            current = next_num
            if is_prime(current):
                return current
        return None
