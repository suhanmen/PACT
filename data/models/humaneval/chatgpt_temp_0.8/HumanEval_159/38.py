def eat(number, need, remaining):
    total_eaten = number + remaining
    if total_eaten >= need:
        remaining = total_eaten - need
        total_eaten = need
    else:
        remaining = 0
    return [total_eaten, remaining]
