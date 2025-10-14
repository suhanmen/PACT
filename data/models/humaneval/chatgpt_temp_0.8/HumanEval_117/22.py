def select_words(s, n):
    if not s:
        return []
    
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    words = []
    
    for word in s.split():
        count = sum(1 for c in word if c in consonants)
        if count == n:
            words.append(word)
    
    return words
