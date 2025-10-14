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
    # First, split the string into a list of lowercase letters
    letters = test.lower().split()

    # Then, create a dictionary to keep track of the count of each letter
    letter_count = {}

    # Loop through each letter and count how many times it appears
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    # Find the maximum count of any letter
    max_count = max(letter_count.values())

    # Create a list of al
