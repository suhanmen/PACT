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
    # initialize an empty dictionary to store the letter frequency
    letter_freq = {}
    
    # split the input string by space
    letters = test.split()
    
    # iterate over each letter in the list of letters
    for letter in letters:
        # if the letter is already in the dictionary, increase its count by 1
        if letter in letter_freq:
            letter_freq[letter] += 1
        # otherwise, add the letter to the dictionary with a count of 1
        else:
            letter_freq[letter] = 1
            
    # find the maximum count of any letter in the dictionary
    max_count = max(letter_freq.values())
    
    # initialize an empty list to store the letters with the maximum count
    max_letters = []
    
    # iterate over each letter in the dictionary
    for letter, count in letter_freq.items():
        # if the count of the letter is equal to the maximum count, add the letter to the list
        if count == max_count:
            max_letters.append(letter)
  
