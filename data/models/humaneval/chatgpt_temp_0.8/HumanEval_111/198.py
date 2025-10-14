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
    
    # Convert the input string to a list of individual letters
    letters = test.split()

    # Create an empty dictionary to store the count of each letter
    count = {}

    # Loop over each letter
    for letter in letters:
        # If the letter is not in the dictionary, add it with a count of 1
        if letter not in count:
            count[letter] = 1
        # If the letter is already in the dictionary, increment its count by 1
        else:
            count[letter] += 1

    # Find the maximum count of any letter in the dictionary
    max_count = max(count.values())

    # Create a new dictionary to store the letters with the maximum count
    result = {}

    # Loop over each letter in the dictionary
    for letter, letter_count in count.items():
        # If the letter's count is equal to the maximum count, add it to the result dictionary
        if letter_count == max_count:
            result[letter] = letter_count

    # Return the result dictionary
    return
