def fib4(n: int):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        # initialize the list with the first four values
        fib_list = [0, 0, 2, 0]
        for i in range(4, n+1):
            # calculate the new value using the previous four values
            new_val = fib_list[i-1] + fib_list[i-2] + fib_list[i-3] + fib_list[i-4]
            # shift the list to the left and add the new value at the end
            fib_list = fib_list[1:] + [new_val]
        return fib_list[-1]
