def eat(number, need, remaining):
    total_eaten = number + remaining if number + remaining < need else need
    remaining_carrots = remaining - (need - number) if remaining >= (need - number) else 0
    return [total_eaten, remaining_carrots]
