def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        # Initialize an array to store the previous 4 values of fib4.
        # We only need to keep track of the last 4 values to compute the next one.
        fib = [0, 0, 2, 0]
        # Iterate from index 4 to n, updating the array with the next value of fib4.
        for i in range(4, n+1):
            # Compute the next value of fib4 using the previous 4 values.
            fib[i%4] = fib[(i-1)%4] + fib[(i-2)%4] + fib[(i-3)%4] + fib[(i-4)%4]
        return fib[n%4]
