def histogram(test):
    freq = {}
    max_count = 0
    for letter in test.split():
        freq[letter] = freq.get(letter, 0) + 1
        max_count = max(max_count, freq[letter])
    result = {letter: count for letter, count in freq.items() if count == max_count}
    return result
