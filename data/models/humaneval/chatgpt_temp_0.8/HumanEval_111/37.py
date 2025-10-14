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
    # split the string into a list of lowercase letters
    letters = test.lower().split()

    # create a dictionary to store the count of each letter
    counts = {}

    # loop over the letters and count how many times each letter appears
    for letter in letters:
        counts[letter] = counts.get(letter, 0) + 1

    # find the maximum count
    max_count = max(counts.values())

    # create a list of letters that have the maximum count
    max_letters = [letter for letter, count in counts.items() if count == max_count]

    # create a dictionary containing the max letters and their counts
    result = {letter: count for letter, count in counts.items() if letter in max_letters}

    return result
