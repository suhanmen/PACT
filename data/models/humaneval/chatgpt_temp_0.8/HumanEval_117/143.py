def select_words(s, n):
    if not s:
        return []
    consonants = set("bcdfghjklmnpqrstvwxyz")
    words = s.split()
    result = []
    for word in words:
        count = 0
        for letter in word:
            if letter.lower() in consonants:
                count += 1
        if count == n:
            result.append(word)
    return result
