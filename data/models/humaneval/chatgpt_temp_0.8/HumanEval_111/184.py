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
    if test == '':
        return {}
    else:
        # split the string into a list of lowercase letters
        letters = test.split()
        # initialize an empty dictionary to store letter counts
        counts = {}
        # loop through the letters and count occurrences
        for letter in letters:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
        # find the maximum count
        max_count = max(counts.values())
        # initialize an empty list to store the letters with the maximum count
        max_letters = []
        # loop through the counts and add letters with the maximum count to the list
        for letter, count in counts.items():
            if count == max_count:
                max_letters.append(letter)
        # create a dictionary of the max letters and their counts
        max_counts = {}
        for letter in max_letters:
            max_counts[letter] = max_count
        retur
