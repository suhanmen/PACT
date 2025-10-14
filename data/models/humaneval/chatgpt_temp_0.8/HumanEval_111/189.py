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
    # Convert the string to a list of lowercase characters
    chars = test.lower().split()
    
    # Create a dictionary to store the frequency of each character
    freq = {}
    
    # Loop through each character and add its frequency to the dictionary
    for char in chars:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
    # Find the maximum frequency
    max_freq = max(freq.values())
    
    # Create a new dictionary containing only the characters with the maximum frequency
    result = {}
    for char, count in freq.items():
        if count == max_freq:
            result[char] = count
    
    return result
