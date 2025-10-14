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
    if not test:
        return {}

    # Create a list of all characters in the input string
    characters = test.split()

    # Create a dictionary to store the frequency count of each character
    frequency = {}

    # Iterate through each character in the list and update the frequency count in the dictionary
    for character in characters:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

    # Find the maximum frequency count
    max_count = max(frequency.values())

    result = {}
    # Iterate through the dictionary again and add all characters with the maximum frequency count to the result dictionary
    for character, count in frequency.items():
        if count == max_count:
            result[character] = count

    return result
