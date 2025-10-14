# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """
    Determines if a person correctly guessed the results of a number of matches.

    Args:
        game: list of int, representing the scores of the matches
        guess: list of int, representing the guesses of the person

    Returns:
        list of int, representing how far off each guess was

    Example:
        compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
        compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return [abs(game[i] - guess[i]) if game[i] != guess[i] else 0 for i in range(len(game))]
