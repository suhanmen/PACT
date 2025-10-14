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
    letters = test.split() # Split the string into a list of letters
    histogram_dict = {} # Create an empty dictionary to store the count of each letter

    for letter in letters:
        if letter in histogram_dict:
            histogram_dict[letter] += 1 # Increment the count of the letter if it's already in the dictionary
        else:
            histogram_dict[letter] = 1 # Add the letter to the dictionary with a count of 1 if it's not already in there
    
    max_count = max(histogram_dict.values()) # Find the maximum count in the dictionary
    
    max_letters = [k for k, v in histogram_dict.items() if v == max_count] # Find all letters with the maximum count
    
    return {k: v for k, v in histogram_dict.items() if k in max_letters} # Return a dictionary containing only the letters with the maximum count
