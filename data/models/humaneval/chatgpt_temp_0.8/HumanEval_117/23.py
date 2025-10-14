def select_words(s, n):
    vowel_set = set('aeiouAEIOU')
    words = s.split()
    result = []
    for word in words:
        consonant_count = sum(1 for letter in word if letter not in vowel_set)
        if consonant_count == n:
            result.append(word)
    return result
