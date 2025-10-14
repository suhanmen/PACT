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

    # Create an empty dictionary to store the counts
    counts = {}

    # Loop through each word in the list
    for word in words:
        # Loop through each letter in the word
        for letter in word:
            # If the letter is not already in the dictionary, add it with a count of 1
            if letter not in counts:
                counts[letter] = 1
            # If the letter is already in the dictionary, increment its count by 1
            else:
                counts[letter] += 1

    # Find the maximum count
    max_count = max(counts.values())

    # Create a new dictionary to store the letters with the maximum count
    result = {}

    # Loop through each letter and count in the dictionary
    for letter, count in counts.items():
        # If the count is equal to the maximum count, add the letter and count to the result dictionary
        if count == max_count:
            result[letter] = c