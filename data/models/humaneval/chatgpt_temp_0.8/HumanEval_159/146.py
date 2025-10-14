def eat(number, need, remaining):
    total_eaten = number + remaining  # start with the number of carrots already eaten
    remaining_carrots = remaining - (need - number)  # subtract the additional carrots needed from the remaining carrots
    
    if remaining_carrots < 0:  # if there are not enough remaining carrots
        remaining_carrots = 0  # eat all remaining carrots
        total_eaten = number + remaining  # and still be hungry
    
    return [total_eaten, remaining_carrots]
