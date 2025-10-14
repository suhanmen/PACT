def count_distinct_characters(string: str) -> int:
    # convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    # use a set to store unique characters
    unique_chars = set()
    # iterate through each character in the string
    for char in string:
        # add the character to the set if it's not already there
        if char not in unique_chars:
            unique_chars.add(char)
    # return the size of the set, which is the number of distinct characters
    return len(unique_chars)
