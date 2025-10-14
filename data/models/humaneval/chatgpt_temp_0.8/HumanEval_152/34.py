# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """
    Determines if a person correctly guessed the results of a number of matches,
    returning an array of the same length denoting how far off each guess was.
    
    :param game: list of scores
    :type game: list
    :param guess: list of guesses
    :type guess: list
    
    :return: list of absolute differences between guess and score
    :rtype: list
    """
    diffs = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            diffs.append(0)
        else:
            diffs.append(abs(game[i] - guess[i]))
    return diffs
