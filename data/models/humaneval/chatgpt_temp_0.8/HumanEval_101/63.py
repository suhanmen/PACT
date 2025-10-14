def words_string(s):
    words = []
    for word in s.split():
        # Remove commas and append each word to the list
        words.append(word.replace(",", ""))
    return words
