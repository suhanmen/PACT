def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ignore case differences
    string = string.lower()
    # Use a set to keep track of distinct characters
    unique_chars = set()
    # Iterate over each character in the string
    for char in string:
        # If the character is not already in the set, add it
        if char not in unique_chars:
            unique_chars.add(char)
    # Return the size of the set, which is the number of distinct characters
    return len(unique_chars)
