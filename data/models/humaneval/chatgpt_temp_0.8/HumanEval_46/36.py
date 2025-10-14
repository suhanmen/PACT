# CANNOT PARSE CODE SNIPPET
def fib4(n: int) -> int:
    sequence = [0, 0, 2, 0]
    if n <= 3:
        return sequence[n]
    for i in range(4, n+1):
        next_num = sum(sequence)
        sequence.pop(0)
        sequence.append(next_num)
    return sequence[3]
