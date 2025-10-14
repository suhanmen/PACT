def words_string(s):
    # Replace commas with spaces to simplify splitting
    s = s.replace(",", " ")
    # Split the string into words
    words = s.split()
    # Return the list of words
    return words
