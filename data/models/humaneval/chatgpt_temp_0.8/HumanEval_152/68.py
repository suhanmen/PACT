# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    diffs = []
    for i in range(len(game)):
        diff = abs(game[i] - guess[i])
        diffs.append(diff)
    return diffs
