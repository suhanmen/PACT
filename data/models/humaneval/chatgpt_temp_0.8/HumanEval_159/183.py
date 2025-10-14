def eat(number, need, remaining):
    # Calculate the total number of eaten carrots after your meals
    total_eaten = number + min(remaining, need)
    
    # Calculate the number of carrots left after your meals
    remaining = max(0, remaining - need)
    
    return [total_eaten, remaining]
