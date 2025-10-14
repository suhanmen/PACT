def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to disregard case sensitivity
    string = string.lower()
    
    # Create a set to store the distinct characters
    distinct_chars = set()
    
    # Iterate through each character in the string and add it to the set
    for char in string:
        distinct_chars.add(char)
    
    # Return the size of the set, which represents the number of distinct characters
    return len(distinct_chars)
