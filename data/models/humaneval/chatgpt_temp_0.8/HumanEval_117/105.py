def select_words(s, n):
    if len(s) == 0:
        return []
    else:
        words = s.split()
        result = []
        for word in words:
            consonants = 0
            for letter in word:
                if letter.isalpha() and letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
                    consonants += 1
            if consonants == n:
                result.append(word)
        return result
