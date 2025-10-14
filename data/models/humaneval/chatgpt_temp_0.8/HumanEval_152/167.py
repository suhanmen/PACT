# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """
    Determines how far off each guess was from the actual score of a match.
    
    Args: 
    - game: list of integers representing the actual scores of matches
    - guess: list of integers representing the guessed scores of matches
    
    Returns:
    - list of integers representing the absolute difference between each guess and actual score. 
      If the guess was correct, the value is 0.
    """
    result = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i] - guess[i]))
    return result
