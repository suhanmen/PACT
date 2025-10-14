# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """
    Determines how far off each guess was from the actual score of a number of matches.

    Args:
        game (list): The actual scores of the matches.
        guess (list): The guesses made for each match.

    Returns:
        list: An array of the same length as 'game' and 'guess', denoting how far off each guess was.
              If the guess was correct, the value is 0. If not, the value is the absolute difference
              between the guess and the score.
    """
    differences = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            differences.append(0)
        else:
            differences.append(abs(game[i] - guess[i]))
    return differences
