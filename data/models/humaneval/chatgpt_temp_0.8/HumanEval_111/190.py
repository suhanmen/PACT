def histogram(test):
    """
    Given a string representing a space separated lowercase letters, return a dictionary of the letter with the most
    repetition and containing the corresponding count. If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """
    if not test:
        return {}

    # Split the string into a list of individual characters
    characters = test.split()

    # Count the frequency of each character
    frequencies = {}
    for char in characters:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    # Find the maximum frequency
    max_frequency = max(frequencies.values())

    # Create a dictionary containing all characters with the maximum frequency
    result = {}
    for cha
