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
    # Split the string into a list of lowercase letters and initialize a dictionary
    letters = test.lower().split()
    result = {}

    # Count the occurrence of each letter and store it in the dictionary
    for letter in letters:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1

    # Find the maximum occurrence of a letter in the dictionary
    max_occurrence = max(result.values())

    # Create a new dictionary containing only the letters with the maximum occurrence
    final_result = {}
    for letter, count in result.items():
        if count == max_occurrence:
            final_result[letter] = count

    return final_result
