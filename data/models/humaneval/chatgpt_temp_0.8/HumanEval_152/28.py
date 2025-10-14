# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """
    Determines if a person correctly guessed the results of a number of matches.
    Returns an array of the same length denoting how far off each guess was.
    If they have guessed correctly, the value is 0, and if not, the value is the
    absolute difference between the guess and the score.

    :param game: list of scores
    :param guess: list of guesses
    :return: list of absolute differences between guess and score
    """
    result = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i] - guess[i]))
    return result
