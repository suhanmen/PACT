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
        dict_count = {}
        list_test = test.split(' ')
        for letter in list_test:
            if letter in dict_count:
                dict_count[letter] += 1
            else:
                dict_count[letter] = 1
        max_count = max(dict_count.values())
        max_letters = [k for k,v in dict_count.items() if v == max_count]
        return {k:v for k,v in dict_count.items() if k in max_letters}
