def histogram(test):
    """
    Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.

    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """
    # Create an empty dictionary to hold the count of each letter
    count = {}

    # Split the string by spaces to get a list of letters
    letters = test.split()

    # Loop through each letter in the list
    for letter in letters:
        # If the letter is not in the dictionary yet, add it with a count of 1
        if letter not in count:
            count[letter] = 1
        # If the letter is already in the dictionary, increment its count
        else:
            count[letter] += 1

    # Find the maximum 
