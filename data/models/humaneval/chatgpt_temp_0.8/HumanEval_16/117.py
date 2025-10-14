def count_distinct_characters(string: str) -> int:
    # convert the string to lowercase to ignore case distinctions
    string = string.lower()
    # create a set of the characters in the string
    char_set = set(string)
    # return the length of the set
    return len(char_set)
