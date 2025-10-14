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
    # Create a dictionary to store the count for each letter
    count_dict = {}
    # Split the test string into a list of lowercase letters
    letters = test.lower().split()
    # Loop through each letter in the list
    for letter in letters:
        # If the letter is already in the dictionary, increment its count
        if letter in count_dict:
            count_dict[letter] += 1
        # Otherwise, add the letter to the dictionary with a count of 1
        else:
            count_dict[letter] = 1
    # Determine the maximum count
    max_count = max(count_dict.values())
    # Create a new dictionary to store the letters with the maximum count
    result_dict = {}
    # Loop through each key-value pair in the count_dict
    for key, value in count_dict.items():
        # If the value is equal to the maximum count, add the key/value pair to the result_dict
        if value == max_count:
            result_dict[key] = value
    # Return the result_dict
    return result_dict
