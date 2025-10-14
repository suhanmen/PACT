def solution(lst):
    sum = 0
    for i in range(1, len(lst), 2): # iterate through even positions
        if lst[i] % 2 == 1: # check if element is odd
            sum += lst[i] # add to sum
    return sum
