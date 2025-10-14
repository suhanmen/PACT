# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """Return an array of the same length denoting how far off each guess was.
    
    Args:
    game -- list of scores
    guess -- list of guesses
    
    Returns:
    list of the same length denoting how far off each guess was
    """
    return [abs(game[i] - guess[i]) if game[i] != guess[i] else 0 for i in range(len(game))]
