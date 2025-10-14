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
    # Convert the string to a list of lowercase letters
    letters = test.lower().split()

    # Create an empty dictionary to store the letter counts
    counts = {}

    # Loop through the letters and count the occurrences of each letter
    for letter in letters:
        counts[letter] = counts.get(letter, 0) + 1

    # Find the maximum count value
    max_count = max(counts.values())

    # Create a new dictionary to store the letters with the maximum count
    max_letters = {letter: count for letter, count in counts.items() if count == max_count}

    return max_letters
