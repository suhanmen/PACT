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
    # split the test string into a list of lowercase letters
    letters = test.lower().split()

    # create an empty dictionary to store the counts of each letter
    counts = {}

    # iterate over each letter in the list
    for letter in letters:
        # if the letter is already in the counts dictionary, increment its count
        if letter in counts:
            counts[letter] += 1
        # otherwise, add the letter to the dictionary with a count of 1
        else:
            counts[letter] = 1

    # find the maximum count of any letter in the dictionary
    max_count = max(counts.values())

    # create an empty list to store the letters with the maximum count
    max_letters = []

    # iterate over each key-value pair in the dictionary
    for letter, count in counts.items():
        # if the count is equal to the maximum count, add the letter to the max_letters list
        if count == max_count:
            max_letters.append(letter)

    # create a dictionary with th
