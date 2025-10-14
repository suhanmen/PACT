# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """
    Determines how far off a person's guesses were from the actual scores of a series of matches.
    
    Args:
    game -- list of actual scores
    guess -- list of guesses
    
    Returns:
    A list of the same length as game and guess, where each element denotes how far off the guess was from the score.
    If the guess was correct, the value is 0. If not, the value is the absolute difference between the guess and the score.
    """
    
    results = []
    
    for i in range(len(game)):
        diff = abs(game[i] - guess[i])
        results.append(diff)
    
    return results
