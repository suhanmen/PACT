def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Replacing commas with spaces to split the string by spaces
    s = s.replace(",", " ")
    # Splitting the string into words
    words = s.split()
    # Returning the list of words
    return words
