def eat(number, need, remaining):
    total_eaten = number + remaining
    remaining_carrots = 0
    if total_eaten >= need:
        remaining_carrots = total_eaten - need
        total_eaten = need
    return [total_eaten, remaining_carrots]
