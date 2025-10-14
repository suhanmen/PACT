def histogram(test):
    counts = {}
    for letter in test.split():
        counts[letter] = counts.get(letter, 0) + 1
    max_count = max(counts.values())
    result = {k: v for k, v in counts.items() if v == max_count}
    return result
