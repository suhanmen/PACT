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
    if test == "":
        return {}
    else:
        test_list = test.split()
        count_dict = {}
        max_value = 0
        for letter in test_list:
            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1
            if count_dict[letter] > max_value:
                max_value = count_dict[letter]
        results = {}
        for letter, count in count_dict.items():
            if count == max_value:
                results[letter] = count
        return results
