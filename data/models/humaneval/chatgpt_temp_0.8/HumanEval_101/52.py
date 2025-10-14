def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    
    # Split the string into words using commas or spaces as delimiters
    words = s.split(", ")
    words = [word.split(" ") for word in words]
    
    # Flatten the list of lists and return the resulting array
    return [word for sublist in words for word in sublist]
