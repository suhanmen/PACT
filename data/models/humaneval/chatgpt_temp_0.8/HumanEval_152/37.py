# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """
    Determines if a person correctly guessed the results of a number of matches.

    Args:
    game: list(int) - array of scores
    guess: list(int) - array of guesses

    Returns:
    list(int) - array of the same length denoting how far off each guess was.
                If they have guessed correctly, the value is 0, and if not,
                the value is the absolute difference between the guess and the score.
    """

    result = []
    for i in range(len(game)):
        diff = abs(game[i] - guess[i])
        result.append(diff)

    return result
