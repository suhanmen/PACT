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
    # create an empty dictionary to store the letter counts
    counts = {}

    # iterate over each letter in the string
    for letter in test.split():
        # if the letter is not already in the dictionary, add it with a count of 1
        if letter not in counts:
            counts[letter] = 1
        # if the letter is already in the dictionary, increment its count
        else:
            counts[letter] += 1

    # find the maximum count
    max_count = max(counts.values())

    # create a new dictionary to store the letters with the maximum count
    max_letters = {}

    # iterate over the letters and counts
    for letter, count in counts.items():
        # if the count is equal to the maximum count, add the letter to the new dictionary
        if count == max_count:
            max_letters[letter] = count

    # return the new dictionary of letters with the maximum count
    return max_letters
