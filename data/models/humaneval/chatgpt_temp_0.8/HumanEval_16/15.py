def count_distinct_characters(string: str) -> int:
    # convert the string to lowercase to ignore case
    string = string.lower()
    
    # use a set to track unique characters
    unique_chars = set()
    
    # loop through each character in the string
    for char in string:
        # add the character to the set
        unique_chars.add(char)
    
    # return the size of the set, which is the number of distinct characters
    return len(unique_chars)
    
