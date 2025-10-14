def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ignore case
    string = string.lower()
    # Use a set to store the distinct characters
    distinct_chars = set(string)
    # Return the size of the set
    return len(distinct_chars)
