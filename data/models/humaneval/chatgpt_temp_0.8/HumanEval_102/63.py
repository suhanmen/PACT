def choose_num(x, y):
    biggest_even = -1 # initially set to -1, in case there's no even number in the range
    
    for i in range(x, y+1): # iterate from x to y inclusive
        if i % 2 == 0: # check if the number is even
            if i > biggest_even: # update the biggest even number found so far
                biggest_even = i
    
    return biggest_even
