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
    # Split the string into a list of lowercase letters
    letters = test.lower().split()
    
    # Create an empty dictionary to store the counts of each letter
    letter_counts = {}
    
    # Loop through each letter in the list
    for letter in letters:
        # If the letter is already in the dictionary, increment its count
        if letter in letter_counts:
            letter_counts[letter] += 1
        # Otherwise, add the letter to the dictionary with a count of 1
        else:
            letter_counts[letter] = 1
    
    # Find the highest count of any letter in the dictionary
    max_count = max(letter_counts.values())
    
    # Create a new dictionary to store the letters with the highest count
    result = {}
    
    # Loop through each letter in the dictionary
    for letter, count in letter_counts.items():
        # If the count equals the highest count, add the letter to the result dictionary
        if count == max_count:
            result[letter] = count
  
