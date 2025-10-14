python
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
    # Create a dictionary to store the counts of each letter
    counts = {}

    # Split the input string into a list of words
    words = test.split()

    # Iterate over each word in the list
    for word in words:
        # Iterate over each letter in the word
        for letter in word:
            # If the letter is not already in the dictionary, add it with a count of 1
            if letter not in counts:
                counts[letter] = 1
            # If the letter is already in the dictionary, increment i
