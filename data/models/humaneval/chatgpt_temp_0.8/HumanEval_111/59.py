def histogram(test):
    counts = {}
    # split the string into a list of letters
    letters = test.split()
    # iterate through each letter and count its occurrences
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    # find the maximum count and create a list of the letters that have that count
    max_count = max(counts.values())
    result = {}
    for letter, count in counts.items():
        if count == max_count:
            result[letter] = count
    return result
