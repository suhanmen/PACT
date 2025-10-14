def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Split the string into words using either commas or spaces as separators
    words = s.split(",") if "," in s else s.split()
    
    # Strip leading and trailing spaces from each word
    words = [word.strip() for word in words]
    
    return words
