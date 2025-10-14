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
    words = [word.strip() for word in words] # Remove any leading or trailing spaces
    
    # Combine the resulting lists and return the array of words
    return " ".join(words).split()
