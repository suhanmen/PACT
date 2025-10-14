def eat(number, need, remaining):
    total_eaten = number + min(remaining, need-number)
    remaining_carrots = max(0, remaining - (need - number))
    return [total_eaten, remaining_carrots]
