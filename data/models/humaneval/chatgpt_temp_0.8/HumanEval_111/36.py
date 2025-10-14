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
    # Convert the string into a list of words
    words = test.split()

    # Create a dictionary to store the count of each letter
    letter_count = {}

    # Loop through each word in the list and count the occurrence of each letter
    for word in words:
        for letter in word:
            letter_count[letter] = letter_count.get(letter, 0) + 1

    # Find the maximum count of any letter
    max_count = max(letter_count.values())

    # Create a new dictionary to store the letters with the most repetition
    most_common_letters = {}

    # Loop through the letter_count dictionary and add any letters with the max count to the new dictionary
    for letter, count in letter_count.items():
        if count == max_count:
            most_common_letters[letter] = count

    return most_common_letters
