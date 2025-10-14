def select_words(s, n):
    if not s:
        return []
    
    words = s.split()
    result = []
    for word in words:
        consonants_count = sum(1 for letter in word.lower() if letter not in "aeiou")
        if consonants_count == n:
            result.append(word)
    
    return result
