def choose_num(x, y):
    biggest_even = -1 # Initialize biggest_even as -1
    for num in range(x, y+1): # Loop through the range [x, y]
        if num % 2 == 0 and num > biggest_even: # Check if the number is even and bigger than the current biggest_even
            biggest_even = num # If it is, update biggest_even
    return biggest_even # Return the final biggest_even value
