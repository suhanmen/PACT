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
    # Split the input string into a list of letters
    letters = test.split()

    # Create an empty dictionary to store the letter counts
    histogram_dict = {}

    # Loop through the letters and count their occurrences
    for letter in letters:
        if letter in histogram_dict:
            histogram_dict[letter] += 1
        else:
            histogram_dict[letter] = 1

    # Find the maximum count
    max_count = max(histogram_dict.values())

    # Create a list of letters with the maximum count
    max_letters = [k for k, v in histogram_dict.items() if v == max_count]

    # Create a dictionary of the letters and their counts
    result_dict = {k: v for k, v in histogram_dict.items() if k in max_letters}

    # Return the result dictionary
    return result_dict
