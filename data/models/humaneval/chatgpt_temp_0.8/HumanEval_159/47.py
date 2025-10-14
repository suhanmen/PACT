def eat(number, need, remaining):
    total_eaten = number + remaining  # eat all remaining carrots first
    remaining = max(0, remaining - (need - number))  # deduct the remaining carrots needed
    total_eaten -= remaining  # update the total number of eaten carrots
    return [total_eaten, remaining]
