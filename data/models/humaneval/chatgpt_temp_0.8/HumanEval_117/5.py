def select_words(s, n):
    if not s:
        return []
    words = s.split()
    result = []
    for word in words:
        consonants_count = sum(1 for letter in word if letter not in "aeiouAEIOU")
        if consonants_count == n:
            result.append(word)
    return result
