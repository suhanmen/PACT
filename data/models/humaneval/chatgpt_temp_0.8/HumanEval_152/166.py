# CANNOT PARSE CODE SNIPPET
def compare(game, guess):
    result = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            result.append(0)
        else:
            diff = abs(game[i] - guess[i])
            result.append(diff)
    return result
