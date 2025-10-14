def words_string(s):
    # Replace commas with spaces so that we can split on spaces
    s = s.replace(",", " ")
    # Split the string on spaces
    words = s.split()
    # Return the resulting array of words
    return words
