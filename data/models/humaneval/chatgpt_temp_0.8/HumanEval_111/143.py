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
    
    # First, split the string into a list of letters
    letters = test.split()
    
    # Create a dictionary to store the letter counts
    count_dict = {}

    # Loop through the list of letters and count the occurrences of each letter
    for letter in letters:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    
    # Find the maximum count in the dictionary
    max_count = max(count_dict.values())
    
    # Create a new dictionary to store the letters with the maximum count
    max_dict = {}
    
    # Loop through the dictionary again and add any letters with the maximum count to the new dictionary
    for letter, count in count_dict.items():
        if count == max_count:
            max_dict[letter] = count
    
    # Return the dictionary containing the most repeated letter(s)
    return max_dict
