def eat(number, need, remaining):
    eaten = number + min(need, remaining)
    left = max(0, remaining - need)
    return [eaten, left]
