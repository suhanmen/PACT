def fib4(n: int):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        # we will use a list to store the previous 4 numbers in the sequence
        prev = [0, 0, 0, 2]
        for i in range(3, n+1):
            # compute the next number in the sequence by summing the previous 4
            curr = prev[0] + prev[1] + prev[2] + prev[3]
            # shift the previous numbers to the right
            prev = [prev[1], prev[2], prev[3], curr]
        return prev[-1]
