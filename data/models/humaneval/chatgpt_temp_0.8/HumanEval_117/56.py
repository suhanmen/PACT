def select_words(s, n):
    if not s:  # s is empty
        return []

    words = s.split()
    result = []
    for word in words:
        consonants_count = sum(1 for c in word if c.isalpha() and c.lower() not in "aeiou")
        if consonants_count == n:
            result.append(word)

    return result
