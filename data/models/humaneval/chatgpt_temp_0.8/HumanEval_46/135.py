def fib4(n: int):
    # Define an array to hold the values of the previous four elements
    # Initialize the first four elements of the array to match the base cases
    # (fib4(0) = 0, fib4(1) = 0, fib4(2) = 2, fib4(3) = 0)
    prev = [0, 0, 2, 0]

    # Compute each subsequent element of the sequence using the formula
    # fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    for i in range(4, n+1):
        prev[i % 4] = prev[(i-1) % 4] + prev[(i-2) % 4] + prev[(i-3) % 4] + prev[(i-4) % 4]

    # Return the final element of the sequence
    return prev[n % 4]
