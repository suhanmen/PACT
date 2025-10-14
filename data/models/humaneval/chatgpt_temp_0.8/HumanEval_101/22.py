def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Split the string into words using spaces and commas as the delimiters
    words = s.split(",")  # Split by commas
    words = [word.strip() for word in words]  # Strip any leading/trailing spaces from each word
    words = " ".join(words)  # Join the words back together with spaces
    words = words.split()  # Split by spaces
    
    return words
