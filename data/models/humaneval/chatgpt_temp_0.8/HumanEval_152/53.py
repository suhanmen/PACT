def compare(game,guess):
    results = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            results.append(0)
        else:
            results.append(abs(game[i] - guess[i]))
    return results
