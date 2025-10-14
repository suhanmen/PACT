def eat(number, need, remaining):
    total = number + remaining
    if total >= need:
        eaten = need
        left = total - need
    else:
        eaten = total
        left = 0
    return [number + eaten, left]
