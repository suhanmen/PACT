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
    
    # create an empty dictionary to store the counts
    counts = {}
    
    # iterate through each word in the list
    for word in words:
        # iterate through each character in the word
        for char in word:
            # check if the character is already in the dictionary
            if char in counts:
                # increment the count for that character
                counts[char] += 1
            else:
                # add the character to the dictionary with a count of 1
                counts[char] = 1
    
    # find the maximum count
    max_count = max(counts.values())
    
    # create a list of all characters with the maximum count
    max_chars = [char for char, count in counts.items() if count == max_count]
    
    # create a dictionary of the characters with the maximum count and their counts
    result = {char: count for char, count in counts.items() if char in max_chars}
    
  
