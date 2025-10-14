# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """
    Determines if a person correctly guessed the results of a number of matches.
    Returns an array of the same length denoting how far off each guess was.
    If they have guessed correctly, the value is 0, and if not, the value is
    the absolute difference between the guess and the score.
    
    :param game: A list of integers representing the scores of the matches
    :param guess: A list of integers representing the guesses for the scores of the matches
    :return: A list of integers representing how far off each guess was
    
    example:
    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    result = []
    
    for i in range(len(game)):
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i] - guess[i]))
            
    return result
