def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.

    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    words = []
    # Split the string by commas or spaces
    split_string = s.split(",") if "," in s else s.split()
    # Loop through each word and append it to the words list
    for word in split_string:
        # Remove any leading or trailing whitespace
        word = word.strip()
        # Append the word to the list if it's not empty
        if word != "":
            words.append(word)
    return words
