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
    # convert string to list of letters
    letters = test.split()
    
    # create dictionary to hold letter counts
    count_dict = {}
    
    # loop through letters and count occurrences
    for letter in letters:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    
    # find max count
    max_count = max(count_dict.values())
    
    # create dictionary of letters with max count
    max_dict = {k: v for k, v in count_dict.items() if v == max_count}
    
    return max_dict
