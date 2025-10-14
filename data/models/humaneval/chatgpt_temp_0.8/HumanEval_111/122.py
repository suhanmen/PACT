def histogram(test):
    counts = {}
    max_count = 0
    for letter in test.split():
        counts[letter] = counts.get(letter, 0) + 1
        if counts[letter] > max_count:
            max_count = counts[letter]

    result = {}
    for letter, count in counts.items():
        if count == max_count:
            result[letter] = count
    return result
