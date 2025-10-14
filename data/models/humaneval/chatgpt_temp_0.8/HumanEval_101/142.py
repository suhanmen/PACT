def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    words = []
    
    # Split the string into words based on commas and spaces
    words = s.split(", ")
    words = [word.split(" ") for word in words]
    words = [word for sublist in words for word in sublist]
    
    return words
