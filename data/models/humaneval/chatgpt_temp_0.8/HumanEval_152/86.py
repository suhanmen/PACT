# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """
    Determines if a person correctly guessed the results of a number of matches. Returns an array of the same length
    denoting how far off each guess was. If they have guessed correctly, the value is 0, and if not, the value is the
    absolute difference between the guess and the score.

    :param game: list of actual scores
    :param guess: list of guessed scores
    :return: list of differences between the actual and guessed scores
    """
    differences = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            differences.append(0)
        else:
            differences.append(abs(game[i] - guess[i]))
    return differences
