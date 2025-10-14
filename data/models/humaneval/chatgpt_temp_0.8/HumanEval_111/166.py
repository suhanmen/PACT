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

    # Split the input string into a list of individual letters
    letters = test.split()

    # Create an empty dictionary to store the counts of each letter
    counts = {}

    # Loop through each letter in the list
    for letter in letters:
        
        # If the letter is already in the counts dictionary, increment its count by 1
        if letter in counts:
            counts[letter] += 1
        # If the letter is not in the counts dictionary, add it with a count of 1
        else:
            counts[letter] = 1

    # Find the maximum count in the counts dictionary
    max_count = max(counts.values())

    # Create an empty dictionary to store the letters with the maximum count
    max_letters = {}

    # Loop through each key and value in the counts dictionary
    for key, value in counts.items():
        
        # If the value is equal to the maximum count, add the key-value pair to the max_letters dictionary
        if value == max_count:
            max_letters[key] 
