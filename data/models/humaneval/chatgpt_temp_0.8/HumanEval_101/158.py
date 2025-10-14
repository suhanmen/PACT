def words_string(s):
    """
    You will be given a string of words separated by commas and/or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # replace commas with spaces
    s = s.replace(",", " ")
    
    # split the string into words using the spaces as the delimiter
    words = s.split()
    
    # return the resulting list of words
    return words
