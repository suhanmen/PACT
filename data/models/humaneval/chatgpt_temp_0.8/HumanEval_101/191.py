def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Split the string into words using spaces and commas as delimiters
    words = s.split(", ")
    words = [w for word in words for w in word.split(" ")]
    
    # Remove any empty strings from the list of words
    words = [w for w in words if w != ""]
    
    return words
