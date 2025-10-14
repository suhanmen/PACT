def select_words(s, n):
    if not s:
        return []
    words = s.split()
    selected = []
    for word in words:
        consonants = sum(1 for letter in word if letter not in "aeiouAEIOU")
        if consonants == n:
            selected.append(word)
    return selected
