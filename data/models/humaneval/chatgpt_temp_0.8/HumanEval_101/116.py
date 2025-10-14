def words_string(s):
    # Split the string into words using ",", " " as delimiters
    words = re.split(',|\s', s)
    
    # Filter out empty strings
    words = filter(lambda w: w != '', words)
    
    # Return the list of words
    return list(words)
