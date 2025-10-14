# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """
    Determines if a person correctly guessed the results of a number of matches.

    Parameters:
    game (list): A list of scores
    guess (list): A list of guesses

    Returns:
    result (list): A list of how far off each guess was
    """

    result = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i] - guess[i]))
    return result
