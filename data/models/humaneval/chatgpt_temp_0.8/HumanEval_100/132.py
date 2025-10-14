def make_a_pile(n):
    pile = [n] # initialize the first level with n stones
    for i in range(1, n):
        if n % 2 == 0: # if n is even
            stones = n + (2 * i) # add 2 to the previous level's stones
        else: # if n is odd
            stones = n + (2 * i - 1) # add 1 to the previous level's stones
        pile.append(stones) # add the stones to the pile
    return pile
