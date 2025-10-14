def choose_num(x, y):
    biggest_even = -1 # initialize the variable
    for num in range(x, y+1): # loop through the range [x, y]
        if num % 2 == 0 and num > biggest_even: # check if num is even and greater than biggest_even
            biggest_even = num # update the variable
    return biggest_even # return the result
