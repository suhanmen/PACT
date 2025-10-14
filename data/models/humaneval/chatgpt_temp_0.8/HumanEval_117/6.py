def select_words(s, n):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    words = s.split()
    result = []
    for word in words:
        if len(word) == 0:
            continue
        num_consonants = 0
        for letter in word:
            if letter in consonants:
                num_consonants += 1
        if num_consonants == n:
            result.append(word)
    return result
