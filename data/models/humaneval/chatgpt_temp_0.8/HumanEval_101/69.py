def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # split the string into words based on commas or spaces
    words = s.split(",") if "," in s else s.split(" ")
    
    # remove any leading/trailing spaces from each word
    words = [word.strip() for word in words]
    
    return words
