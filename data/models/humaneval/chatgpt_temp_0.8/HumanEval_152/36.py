# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    difference = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            difference.append(0)
        else:
            difference.append(abs(game[i] - guess[i]))
    return difference
