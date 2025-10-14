def compare(game,guess):
    distances = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            distances.append(0)
        else:
            distances.append(abs(game[i] - guess[i]))
    return distances
