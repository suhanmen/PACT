# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    """
    Determines if a person correctly guessed the results of a number of matches.

    :param game: list of scores
    :param guess: list of guesses
    :return: list of the same length denoting how far off each guess was

    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    off_by = []

    for i in range(len(game)):
        diff = abs(game[i] - guess[i])
        off_by.append(diff)

    return off_by
