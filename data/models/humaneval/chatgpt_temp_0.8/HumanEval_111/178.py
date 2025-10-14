def histogram(test):
    # Create an empty dictionary to store letter counts
    counts = {}
    
    # Split the input string into individual letters
    letters = test.split()
    
    # Loop through each letter
    for letter in letters:
        # If the letter is already in the counts dictionary, increment its count
        if letter in counts:
            counts[letter] += 1
        # Otherwise, add the letter to the dictionary with a count of 1
        else:
            counts[letter] = 1
    
    # Find the highest count of any letter in the dictionary
    max_count = max(counts.values())
    
    # Create a new dictionary to store the letters with the highest count
    result = {}
    
    # Loop through each letter and count in the counts dictionary
    for letter, count in counts.items():
        # If the count is equal to the highest count, add the letter and count to the result dictionary
        if count == max_count:
            result[letter] = count
    
    # Return the result dictionary
