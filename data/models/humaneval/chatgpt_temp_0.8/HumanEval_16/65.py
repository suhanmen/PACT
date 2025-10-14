def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ignore case
    string = string.lower()
    # Create an empty set to hold the distinct characters
    distinct_chars = set()
    # Iterate through each character in the string
    for char in string:
        # Add the character to the set
        distinct_chars.add(char)
    # Return the number of distinct characters in the set
    return len(distinct_chars)
