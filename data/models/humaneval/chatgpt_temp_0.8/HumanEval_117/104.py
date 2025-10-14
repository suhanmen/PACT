def select_words(s, n):
    vowels = 'aeiouAEIOU'
    words = s.split()
    result = []
    for word in words:
        consonants_count = 0
        for letter in word:
            if letter not in vowels:
                consonants_count += 1
        if consonants_count == n:
            result.append(word)
    return result
