def count_consonants(word):
    """Helper function that counts the number of consonants in a word."""
    consonants = "bcdfghjklmnpqrstvwxyz"
    return len([c for c in word if c.lower() in consonants])

def select_words(s, n):
    """Given a string s and a natural number n, returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    if not s:
        return []
    words = s.split()
    result = []
    for w in words:
        if count_consonants(w) == n:
            result.append(w)
    return result
