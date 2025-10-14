def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    if not test:
        return {}
    # split the input into a list of lowercase letters
    letters = test.lower().split()
    # create an empty dictionary to store the count of each letter
    counts = {}
    # iterate over the letters and count their occurrences
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    # find the highest count
    max_count = max(counts.values())
    # create a dictionary to store the letters with the highest count
    result = {}
    for letter, count in counts.items():
        if count == max_count:
            result[letter] = count
    return result
