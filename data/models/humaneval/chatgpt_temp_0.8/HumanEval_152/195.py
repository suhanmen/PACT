# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    diffs = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            diffs.append(0)
        else:
            diffs.append(abs(game[i] - guess[i]))
    return diffs
