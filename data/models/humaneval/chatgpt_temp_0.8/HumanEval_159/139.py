def eat(number, need, remaining):
    total_eaten = number + min(need, remaining)
    left_over = max(0, remaining - need)

    return [total_eaten, left_over]
