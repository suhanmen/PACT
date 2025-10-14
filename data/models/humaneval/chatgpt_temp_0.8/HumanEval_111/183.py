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
    # Split the input string into a list of individual letters
    letters = test.split()
    # Iterate through the letters and count their occurrences
    for letter in letters:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    # Find the maximum count of any letter
    max_count = max(count_dict.values())
    # Create a new dictionary to hold the letters with the maximum count
    max_letters = {}
    # Iterate through the count dictionary and add any letters with the maximum count to the new dictionary
    for letter, count in count_dict.items():
        if count == max_count:
            max_letters[letter] = count
    return max_letters
