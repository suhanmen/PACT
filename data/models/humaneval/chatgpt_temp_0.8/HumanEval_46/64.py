# CANNOT PARSE CODE SNIPPET
def fib4(n: int) -> int:
    sequence = [0, 0, 2, 0]
    if n < 4:
        return sequence[n]
    for i in range(4, n+1):
        sequence[i % 4] = sum(sequence)  # update cyclically
    return sequence[n % 4]
