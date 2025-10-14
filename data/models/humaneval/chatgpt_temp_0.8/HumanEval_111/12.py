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
    # create an empty dictionary to store the letter counts
    counts = {}
    
    # split the input string by space and iterate over the resulting list
    for letter in test.split():
        
        # if the letter is not already in the dictionary, add it with a count of 1
        if letter not in counts:
            counts[letter] = 1
            
        # if the letter is already in the dictionary, increment its count by 1
        else:
            counts[letter] += 1
            
    # find the maximum count value in the dictionary
    max_count = max(counts.values())
    
    # create a list of all letters that have the maximum count
    max_letters = [letter for letter, count in counts.items() if count == max_count]
    
    # create a dictionary containing the max_letters and their counts
    result = {letter: count for letter, count in counts.items() if letter in max_letters}
    
    return result
