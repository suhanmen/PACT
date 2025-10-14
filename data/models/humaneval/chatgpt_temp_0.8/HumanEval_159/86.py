def eat(number, need, remaining):
    total = number + remaining  # Calculate total number of carrots available
    if total >= need:
        eaten = need  # If there are enough carrots, eat the required number of carrots
    else:
        eaten = total  # Otherwise, eat all the remaining carrots
    remaining = remaining - (eaten - number)  # Calculate the number of carrots left after the meal
    return [number + eaten, max(0, remaining)]  # Return the total number of eaten carrots and the remaining carrots after the meal
