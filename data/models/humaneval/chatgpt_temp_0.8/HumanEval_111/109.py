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
    # First, split the string into a list of individual letters
    letters = test.split()
    
    # Create an empty dictionary to store the letter counts
    counts = {}
    
    # Loop through each letter and add it to the dictionary, incrementing the count if it already exists
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    
    # Find the maximum count value
    max_count = max(counts.values())

    # Create an empty list to store the letters that have the maximum count
    max_letters = []
    
    # Loop through the dictionary to find all letters that have the maximum count
    for letter, count in counts.items():
        if count == max_count:
            max_letters.append(letter)
    
    # Create a dictionary with the letters that have the maximum count and their corresponding counts
    result = {}
    for letter in max_letters:
        result[letter] = max_count
    
    # Return the 
