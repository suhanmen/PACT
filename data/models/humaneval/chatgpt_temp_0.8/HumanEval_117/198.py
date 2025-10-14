def select_words(s, n):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    words = s.split()
    selected_words = []
    for word in words:
        if len(word) == 0:
            continue
        count = 0
        for char in word:
            if char in consonants:
                count += 1
        if count == n:
            selected_words.append(word)
    return selected_words
