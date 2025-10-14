def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.

    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    words = []
    # Split the string on commas and spaces
    split_s = s.split(", ") if ", " in s else s.split()
    for word in split_s:
        # Remove any leading or trailing spaces
        word = word.strip()
        # Add the word to the list if it's not empty
        if word:
            words.append(word)
    return words
