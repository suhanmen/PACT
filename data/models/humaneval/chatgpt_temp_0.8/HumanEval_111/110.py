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
    # Create a dictionary to hold the count of each letter
    count_dict = {}

    # Split the string by space and iterate over each letter
    for letter in test.split(" "):
        # If letter already exists, increment the count by 1
        if letter in count_dict:
            count_dict[letter] += 1
        # If letter doesn't exist, add it to the dictionary with count 1
        else:
            count_dict[letter] = 1

    # Find the maximum count of a letter in the dictionary
    max_count = max(count_dict.values())

    # Create a new dictionary with letters having maximum count
    max_count_dict = {letter: count for letter, count in count_dict.items() if count == max_count}

    # Return the dictionary with letters having maximum count
    return max_count_dict
