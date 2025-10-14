def words_string(s):
    # Split the string into words
    words = s.split()
    # Remove any commas from each word
    words = [word.replace(',', '') for word in words]
    # Return the array of words
    return words
