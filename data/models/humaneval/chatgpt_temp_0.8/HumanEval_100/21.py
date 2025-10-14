def make_a_pile(n):
    # Initialize the list with the first level having n stones
    pile = [n]
    # Initialize the current level with n stones
    current_level = n
    # Loop through n levels
    for i in range(n-1):
        # Determine the number of stones in the next level
        if current_level % 2 == 0:
            next_level = current_level + 1
        else:
            next_level = current_level + 2
        # Add the number of stones in the next level to the pile
        pile.append(next_level)
        # Update the current level
        current_level = next_level
    return pile
