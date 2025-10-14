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
    # Convert the string into a list of lowercase letters
    letters = test.lower().split()
    
    # Create an empty dictionary to store the letter counts
    letter_counts = {}
    
    # Loop through the letters and count their occurrences
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    # Find the maximum count of any letter
    max_count = max(letter_counts.values())
    
    # Create a list of letters that have the maximum count
    max_letters = [letter for letter, count in letter_counts.items() if count == max_count]
    
    # Create a dictionary of the max letters and their counts
    max_counts = {letter: count for letter, count in letter_counts.items() if count == max_count}
    
    return max_counts
