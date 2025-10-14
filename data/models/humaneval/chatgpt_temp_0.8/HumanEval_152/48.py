# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    differences = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            differences.append(0)
        else:
            differences.append(abs(game[i] - guess[i]))
    return differences
