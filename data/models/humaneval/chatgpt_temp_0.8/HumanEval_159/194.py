def eat(number, need, remaining):
    total_eaten = number + remaining
    remaining_carrots = 0

    if total_eaten >= need:
        total_eaten = need
    else:
        remaining_carrots = need - total_eaten
        total_eaten = need

        if remaining_carrots > remaining:
            remaining_carrots = remaining

    return [total_eaten, remaining - remaining_carrots]
