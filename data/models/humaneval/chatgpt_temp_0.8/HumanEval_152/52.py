# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """
    Compare the guesses with the actual scores of the matches and return an array
    of the same length denoting how far off each guess was.

    :param game: a list of actual scores of matches.
    :param guess: a list of guessed scores of matches.
    :return: a list of absolute difference between the guess and the score of each match.
    """
    diff = []

    for i in range(len(game)):
        if game[i] == guess[i]:
            diff.append(0)
        else:
            diff.append(abs(game[i] - guess[i]))

    return diff
