def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Split the string into words by commas or spaces
    words = s.split(",") # split by commas
    words = [w.strip() for w in words] # strip whitespace from each word
    words = " ".join(words).split() # join words back into a string and split by spaces
    
    # Return the array of words
    return words
