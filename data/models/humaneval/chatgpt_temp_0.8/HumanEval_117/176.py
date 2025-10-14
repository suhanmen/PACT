def select_words(s, n):
    if not s:
        return []
    words = s.split()
    result = []
    for word in words:
        consonant_count = 0
        for letter in word:
            if letter.lower() not in "aeiou" and letter.isalpha():
                consonant_count += 1
        if consonant_count == n:
            result.append(word)
    return result
