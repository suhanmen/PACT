def eat(number, need, remaining):
    total_eaten_carrots = number + min(need, remaining)
    carrots_left = max(0, remaining - need)
    return [total_eaten_carrots, carrots_left]
