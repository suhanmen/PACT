def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Split the string into words using both commas and spaces as separators
    words = s.split(",") # Split the string by commas
    words = [word.strip() for word in words] # Remove any leading or trailing spaces from each word
    
    # Now join the split words back together using the space character as the separator
    words = " ".join(words)
    
    # Split the joined string of words using spaces as the separator
    words = words.split()
    
    return words
