def histogram(test):
    """
    Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    """
    # Split the string into a list of lowercase letters
    letters = test.lower().split()
    
    # Create an empty dictionary to store the letter counts
    counts = {}
    
    # Iterate through the list of letters and count the occurrences of each letter
    for letter in letters:
        counts[letter] = counts.get(letter, 0) + 1
    
    # Find the maximum count value
    max_count = max(counts.values())
    
    # Create a new dictionary to store the letters with maximum count
    result = {letter: count for letter, count in counts.items() if count == max_count}
    
    return result
