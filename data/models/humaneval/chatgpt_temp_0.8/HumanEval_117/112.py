def count_consonants(word):
    """Given a word, returns the number of consonants in the word."""
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for c in word if c in consonants)

def select_words(s, n):
    """Given a string s and a natural number n, returns a list of all words from string s 
    that contain exactly n consonants, in order these words appear in the string s."""
    words = s.split()
    result = []
    for w in words:
        if count_consonants(w) == n:
            result.append(w)
    return result
