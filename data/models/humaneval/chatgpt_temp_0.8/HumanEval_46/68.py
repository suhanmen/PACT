# CANNOT PARSE CODE SNIPPET
def fib4(n: int) -> int:
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        fibs = [0, 0, 2, 0]
        for i in range(4, n+1):
            fibs[i % 4] = fibs[(i-1) % 4] + fibs[(i-2) % 4] + fibs[(i-3) % 4] + fibs[(i-4) % 4]
        return fibs[n % 4]
