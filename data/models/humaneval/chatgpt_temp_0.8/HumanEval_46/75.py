# CANNOT PARSE CODE SNIPPET
def fib4(n: int) -> int:
    # Define the base cases
    fib_list = [0, 0, 2, 0]

    # Compute the sequence iteratively
    for i in range(4, n+1):
        # Compute the next element based on the previous 4 elements
        next_fib = fib_list[i-1] + fib_list[i-2] + fib_list[i-3] + fib_list[i-4]

        # Add the next element to the list
        fib_list.append(next_fib)

    # Return the n-th element of the sequence
    return fib_list[n]
