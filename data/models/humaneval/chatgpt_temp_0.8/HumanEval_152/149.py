# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """Compares the guesses with the actual scores for a series of matches.

    Args:
        game (list of int): List of actual scores.
        guess (list of int): List of guesses.

    Returns:
        list of int: List of differences between guesses and actual scores.
    """
    result = []
    for i in range(len(game)):
        diff = abs(game[i] - guess[i])
        result.append(diff)
    return result
