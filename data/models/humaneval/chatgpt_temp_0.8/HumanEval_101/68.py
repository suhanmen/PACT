def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.

    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # split the string by comma or space
    words_list = s.split(",") if "," in s else s.split()

    # strip any leading/trailing whitespaces in each word
    words_list = [word.strip() for word in words_list]

    return words_list
