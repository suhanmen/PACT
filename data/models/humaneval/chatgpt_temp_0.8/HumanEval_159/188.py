def eat(number, need, remaining):
    total_eaten = min(number + need, remaining + number)
    carrots_left = max(remaining - (need - (total_eaten - number)), 0)
    return [total_eaten, carrots_left]
