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
    if test.strip() == "": # if the string is empty return an empty dictionary
        return {}
    else:
        # create a dictionary to store the count of each letter
        count_dict = {}
        # split the string into a list of individual letters
        letters = test.split()
        for letter in letters:
            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1
        # find the highest count of any letter
        max_count = max(count_dict.values())
        # create a list of letters that have the highest count
        max_letters = [k for k, v in count_dict.items() if v == max_count]
        # create a dictionary containing only the letters with the highest count
        result_dict = {k: v for k, v in count_dict.items() if k in max_letters}
        return result_dict
