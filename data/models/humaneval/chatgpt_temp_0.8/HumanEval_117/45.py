def select_words(s, n):
    if not s:
        return []
    
    words = s.split()
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    selected_words = []
    
    for word in words:
        count = 0
        for letter in word:
            if letter in consonants:
                count += 1
        if count == n:
            selected_words.append(word)
            
    return selected_words
