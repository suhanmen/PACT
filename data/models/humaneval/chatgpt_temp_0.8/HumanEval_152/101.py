def compare(game,guess):
    results = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            results.append(0)
        else:
            diff = abs(game[i] - guess[i])
            results.append(diff)
    return results
