# CANNOT PARSE CODE SNIPPET
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    fibonacci = [0, 1]
    while len(fibonacci) < n + 1:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    for i in range(2, len(fibonacci)):
        if is_prime(fibonacci[i]):
            return fibonacci[i]
