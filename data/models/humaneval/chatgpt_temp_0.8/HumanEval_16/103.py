def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    """
    # Convert the string to lowercase
    string = string.lower()
    
    # Create a set of characters in the string
    char_set = set(string)
    
    # Return the length of the set
    return len(char_set)
