def eat(number, need, remaining):
    total_eaten = number + min(remaining, need-number)
    carrots_left = max(0, remaining - (need-number))
    return [total_eaten, carrots_left]
