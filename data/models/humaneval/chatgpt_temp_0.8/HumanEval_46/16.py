# CANNOT PARSE CODE SNIPPET
python
def fib4(n: int) -> int:
    if n == 0 or n == 1:  # base case
        return 0
    elif n == 2:  # base case
        return 2
    else:
        # initialize the sequence with the first 4 elements
        seq = [0, 0, 2, 0]
        for i in range(4, n+1):
            # compute the next element using the formula
            seq[i % 4] = sum(seq)  # circular buffer trick
        return seq[n % 4]
