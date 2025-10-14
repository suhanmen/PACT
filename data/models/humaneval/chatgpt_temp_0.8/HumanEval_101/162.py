def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # split the string into words using commas and spaces as delimiters
    words = s.split(",") # split by commas first
    words = [w.strip() for w in words] # remove leading/trailing spaces from each word
    words = " ".join(words).split() # join the list of words with spaces, then split using spaces as delimiter
    return words
