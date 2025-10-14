# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """
    Determine if a person correctly guessed the results of a number of matches.

    Args:
        game (list): A list of integers representing the scores of the matches.
        guess (list): A list of integers representing the guesses of the matches.

    Returns:
        list: A list of integers representing how far off each guess was. If a guess is correct,
        the value is 0, and if not, the value is the absolute difference between the guess and the score.
    """
    result = []
    for i in range(len(game)):
        diff = abs(game[i] - guess[i])
        result.append(diff if diff != 0 else 0)
    return result
