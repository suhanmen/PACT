def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.

    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Split the string by spaces and commas.
    words = s.split(' ') + s.split(',')

    # Remove any empty strings from the list of words.
    words = [word for word in words if word != '']

    # Return the list of words.
    return words
