def compare(game,guess):
    # initialize an empty result array
    result = []

    # loop through each match in the game and guess arrays
    for i in range(len(game)):
        # calculate the absolute difference between the guess and the score
        diff = abs(guess[i] - game[i])

        # add the difference to the result array
        result.append(diff)

    # return the result array
    return result
