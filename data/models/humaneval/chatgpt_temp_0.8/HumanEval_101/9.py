def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Split the input string into words using commas and spaces as delimiters
    words = s.split(",")  # Split the string using commas first
    words = [word.strip() for word in words]  # Remove leading/trailing spaces from each word
    words = " ".join(words).split()  # Join the words with a space and split them again using spaces
    
    # Return the resulting list of words
    return words
