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
    # Split the string into a list of words
    words = test.split()

    # Count the occurrences of each word in the list
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    # Find the maximum count
    max_count = max(counts.values())

    # Create a dictionary of words with the maximum count
    result = {}
    for word, count in counts.items():
        if count == max_count:
            result[word] = count

    return result
