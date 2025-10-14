def eat(number, need, remaining):
    total_carrots = number + remaining
    if total_carrots >= need:
        eaten_carrots = need
        remaining_carrots = total_carrots - need
    else:
        eaten_carrots = total_carrots
        remaining_carrots = 0
    return [number + eaten_carrots, remaining_carrots]
