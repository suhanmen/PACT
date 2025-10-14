def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ignore case differences
    string = string.lower()
    # Use a set to store unique characters
    unique_chars = set()
    # Iterate through each character of the string
    for char in string:
        # Add the lowercase version of the character to the set
        unique_chars.add(char.lower())
    # Return the size of the set (i.e., the number of distinct characters)
    return len(unique_chars)
