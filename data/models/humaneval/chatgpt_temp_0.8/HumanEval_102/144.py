def choose_num(x, y):
    # Initialize the biggest even integer to be -1
    biggest_even = -1
    
    # Iterate through the range of numbers from x to y inclusive
    for num in range(x, y+1):
        # Check if the current number is even and bigger than the current biggest_even
        if num % 2 == 0 and num > biggest_even:
            biggest_even = num
    
    # Return the biggest_even if it's not -1, otherwise return -1
    return biggest_even if biggest_even != -1 else -1
