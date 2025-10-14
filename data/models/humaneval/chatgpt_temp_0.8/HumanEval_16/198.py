def count_distinct_characters(string: str) -> int:
    # Convert the string to lower case
    string = string.lower()
    # Create an empty set to store the distinct characters
    distinct_chars = set()
    # Iterate through each character in the string
    for char in string:
        # If the character is not in the distinct_chars set, add it
        if char not in distinct_chars:
            distinct_chars.add(char)
    # Return the length of the distinct_chars set
    return len(distinct_chars)
