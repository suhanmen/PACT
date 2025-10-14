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
    letters = test.split()
    
    # Initialize an empty dictionary to store the count of each letter
    counts = {}
    
    # Loop through each letter and update the count in the dictionary
    for letter in letters:
        counts[letter] = counts.get(letter, 0) + 1
    
    # Find the maximum count
    max_count = max(counts.values() or [0])
    
    # Initialize an empty dictionary to store the letters with the maximum count
    max_letters = {}
    
    # Loop through the dictionary and add any letters with the maximum count to the max_letters dictionary
    for letter, count in counts.items():
        if count == max_count:
            max_letters[letter] = count
    
    # Return the max_letters dictionary
    return max_letters
