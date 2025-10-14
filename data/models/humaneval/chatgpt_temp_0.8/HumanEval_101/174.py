def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Split the string into words based on commas and spaces
    words = s.split(",")    # Split by commas
    words = [word.strip() for word in words]    # Remove leading/trailing whitespaces
    words = " ".join(words).split()    # Join by spaces and split into individual words
    
    return words
