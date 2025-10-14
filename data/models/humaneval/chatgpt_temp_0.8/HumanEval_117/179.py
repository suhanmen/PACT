def select_words(s, n):
    if not s:
        return []
    result = []
    for word in s.split():
        consonants = [letter for letter in word if letter not in "aeiouAEIOU"]
        if len(consonants) == n:
            result.append(word)
    return result
