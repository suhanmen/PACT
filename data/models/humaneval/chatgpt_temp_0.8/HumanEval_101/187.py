def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Split the string into words using commas and spaces as delimiters
    words = s.split(", ")
    words = [word.strip() for word in words]  # Remove any leading or trailing whitespace
    
    # If there are no commas, split the string again using spaces as delimiters
    if len(words) == 1:
        words = s.split(" ")
    
    return words
