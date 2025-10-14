def words_string(s):
    # Split the string into words using both commas and spaces as delimiters
    words = s.replace(",", " ").strip().split()

    # Return the array of words
    return words
