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
    # Initialize an empty dictionary to hold the counts for each letter
    counts = {}

    # Split the input string into individual letters
    letters = test.split()

    # Loop through each letter and update its count in the dictionary
    for letter in letters:
        counts[letter] = counts.get(letter, 0) + 1

    # Find the highest count
    max_count = max(counts.values())

    # Initialize an empty dictionary to hold the letters with the highest count
    result = {}

    # Loop through each letter and check if its count matches the highest count
    for letter, count in counts.items():
        if count == max_count:
            result[letter] = count

    # Return the result dictionary
    return result
