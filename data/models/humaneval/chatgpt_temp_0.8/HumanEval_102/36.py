def choose_num(x, y):
    max_even = -1 # initialize the maximum even number to -1
    
    for num in range(x, y+1): # iterate over the range [x, y]
        if num % 2 == 0 and num > max_even: # check if num is even and greater than current max_even
            max_even = num # update max_even to num
    
    return max_even
