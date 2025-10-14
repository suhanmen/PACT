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
    words = test.split()  # Split the input string into words
    counts = {}  # Create an empty dictionary for the counts

    # Loop through each word in the list of words
    for word in words:
        # If the word is not already in the dictionary, set its count to 1
        if word not in counts:
            counts[word] = 1
        # If the word is already in the dictionary, increment its count by 1
        else:
            counts[word] += 1

    # Find the maximum count in the dictionary
    max_count = max(
