def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Split the string into words using the split() function
    words = s.split()
    
    # Iterate through each word in the list of words
    for i in range(len(words)):
        # Remove any commas or other non-word characters from the word
        words[i] = words[i].strip(",.")
    
    # Return the list of cleaned words
    return words
