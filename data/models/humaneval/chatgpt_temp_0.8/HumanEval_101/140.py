def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # split the string into individual words using comma and space as separators
    words_list = s.split(", ")
    # if there are no commas, split the string using space as the separator
    if len(words_list) == 1:
        words_list = s.split()
    # remove any leading or trailing spaces from each word
    words_list = [word.strip() for word in words_list]
    return words_list
