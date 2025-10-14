# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    # Create an empty array to store the differences between each guess and actual score
    result = []
    
    # Iterate through each match
    for i in range(len(game)):
        # If the guess is correct, add 0 to the result array
        if game[i] == guess[i]:
            result.append(0)
        # If the guess is incorrect, add the absolute difference between the guess and actual score to the result array
        else:
            result.append(abs(game[i] - guess[i]))
    
    # Return the array of differences
    return result
