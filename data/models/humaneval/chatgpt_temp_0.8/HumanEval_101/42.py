def words_string(s):
    words = s.split() # split the string on spaces by default
    words = [word.replace(',', '') for word in words] # remove commas from each word
    return words
