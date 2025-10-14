# CANNOT PARSE CODE SNIPPET
def compare(scores, guesses):
    """
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    """
    result = []
    for i in range(len(scores)):
        if scores[i] == guesses[i]:
            result.append(0)
        else:
            result.append(abs(scores[i] - guesses[i]))
    return result
