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
    # Initialize an empty dictionary to store the count of each letter
    counts = {}
    
    # Split the input string into a list of letters
    letters = test.split()
    
    # Loop through each letter and update the count in the dictionary
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
            
    # Find the maximum count value
    max_count = max(counts.values())
    
    # Initialize an empty dictionary to store the letters with the maximum count value
    max_letters = {}
    
    # Loop through each letter and add it to the max_letters dictionary if its count equals max_count
    for letter, count in counts.items():
        if count == max_count:
            max_letters[letter] = count
            
    # Return the max_letters dictionary
    return max_letters
