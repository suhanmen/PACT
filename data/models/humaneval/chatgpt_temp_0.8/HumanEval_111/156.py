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
    # convert the string to a list of lowercase letters
    letters = test.lower().split()
    
    # create a dictionary to store the histogram
    histogram_dict = {}
    
    # loop through the list of letters and count the occurrences of each letter
    for letter in letters:
        if letter in histogram_dict:
            histogram_dict[letter] += 1
        else:
            histogram_dict[letter] = 1
    
    # find the maximum count
    max_count = max(histogram_dict.values())
    
    # create a list of lette
