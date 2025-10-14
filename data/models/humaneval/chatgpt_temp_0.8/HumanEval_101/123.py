def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    
    # Split the string into words based on commas and spaces
    words = s.split(", ")
    words = [w.split(" ") for w in words]
    
    # Flatten the nested list of words
    flattened = [item for sublist in words for item in sublist]
    
    return flattened
