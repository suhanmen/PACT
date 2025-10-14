def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ignore case
    string = string.lower()
    # Use a set to store distinct characters
    distinct_chars = set()
    # Iterate through the string and add each character to the set
    for char in string:
        distinct_chars.add(char)
    # Return the size of the set, which is the number of distinct characters
    return len(distinct_chars)
