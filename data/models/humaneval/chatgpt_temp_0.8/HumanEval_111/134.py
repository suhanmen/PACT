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

    # Create an empty dictionary
    counts = {}

    # Loop through each word in the list
    for word in words:
        # Loop through each character in the word
        for char in word:
            # If the character is not in the dictionary, add it with a count of 1
            if char not in counts:
                counts[char] = 1
            # If the character is already in the dictionary, increment its count by 1
            else:
                counts[char] += 1

    # Find the maximum count
    max_count = max(counts.values())

    # Create a list of all characters with the maximum count
    result = {}
    for char, count in counts.items():
        if count == max_count:
            result[char] = count

    # Return the result
    return result
