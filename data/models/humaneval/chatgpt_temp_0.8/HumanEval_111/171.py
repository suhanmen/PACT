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
    hist_dict = {}
    if len(test) == 0:
        return hist_dict
    
    # split the string by spaces
    split_test = test.split(' ')
    
    # count the occurrence of each letter
    for letter in split_test:
        if letter in hist_dict:
            hist_dict[letter] += 1
        else:
            hist_dict[letter] = 1
    
    # find the maximum count of any letter
    max_count = max(hist_dict.values())
    
    # create a dictionary of all letters with the maximum count
    result_dict = {k:v for k,v in hi
