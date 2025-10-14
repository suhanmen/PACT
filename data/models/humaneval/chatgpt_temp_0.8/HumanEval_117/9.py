def select_words(s, n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = s.split()
    result = []
    for word in words:
        consonant_count = 0
        for letter in word:
            if letter.lower() not in vowels:
                consonant_count += 1
        if consonant_count == n:
            result.append(word)
    return result
