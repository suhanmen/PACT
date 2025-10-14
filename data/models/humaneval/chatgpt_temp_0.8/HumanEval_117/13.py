def select_words(s, n):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    words = s.split()
    result = []
    for word in words:
        if len(word) >= n:
            count = 0
            for letter in word:
                if letter in consonants:
                    count += 1
            if count == n:
                result.append(word)
    return result
