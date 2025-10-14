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
    # split the test string into a list of words
    words = test.split()

    # create a dictionary to store the counts of each letter
    counts = {}

    # loop through each word in the list
    for word in words:
        # loop through each letter in the word
        for letter in word:
            # if the letter is already in the dictionary, increment the count
            if letter in counts:
                counts[letter] += 1
            # if the letter is not in the dictionary, add it with a count of 1
            else:
                counts[letter] = 1

    # create a list of tuples containing the counts and letters
    count_letter_pairs = [(count, letter) for letter, count in counts.items()]

    # sort the list in descending order by count
    count_letter_pairs.sort(reverse=True)

    # create a dictionary to store the result
    result = {}

    # get the highest count
    highest_count = count_letter_pairs[0][0]

    # loop through the list of count/letter tuples
   
