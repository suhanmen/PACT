# CANNOT PARSE
def histogram(test):
    # Split the input string into a list of words
    words = test.split()
    
    # Create an empty dictionary to store the occurrences of each letter
    occurrences = {}
    
    # Loop through each word in the list
    for word in words:
        # Loop through each letter in the word
        for letter in word:
            # If the letter is already in the dictionary, increment its count
            if letter in occurrences:
                occurrences[letter] += 1
            # If the letter is not in the dictionary, add it with a count of 1
            else:
                occurrences[letter] = 1
    
    # Find the maximum count of any letter in the dictionary
    max_count = max(occurrences.values())
    
    # Create an empty dictionary to store the letters with the maximum count
    max_letters = {}
    
    # Loop through each item in the occurrences dictionary
    for letter, count in occurrences.items():
        # If the count is equal to the maximum count, add the letter and count to the max_letters dictionary
        if count == max_count:
            max_letters[letter] = count
            
    # Return the max_letters dictionary
    return max_letters
