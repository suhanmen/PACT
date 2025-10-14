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
    # split the string into a list of words
    words = test.split()

    # initialize an empty dictionary to store letter count
    count_dict = {}

    # loop through each word and each letter in the word
    for word in words:
        for letter in word:
            # if the letter is not yet in the dictionary, add it with a count of 1
            if letter not in count_dict:
                count_dict[letter] = 1
            # if the letter is already in the dictionary, increment its count by 1
            else:
                count_dict[letter] += 1

    # find the maximum count value
    max_count = max(count_dict.values())

    # initialize an empty list to store letters with max count
    max_letters = []

    # loop through each (key, value) pair in the dictionary
    for key, value in count_dict.items():
        # if the value matches the max count, append the key to the list
        if value == max_count:
            max_letters.append(key)

    # initialize an empty dicti
