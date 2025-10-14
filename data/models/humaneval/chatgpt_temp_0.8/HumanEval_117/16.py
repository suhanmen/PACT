def select_words(s, n):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    words = s.split()
    output = []
    for word in words:
        count = 0
        for letter in word:
            if letter in consonants:
                count += 1
        if count == n:
            output.append(word)
    return output
