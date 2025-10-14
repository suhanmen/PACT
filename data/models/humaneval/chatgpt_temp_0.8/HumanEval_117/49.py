def select_words(s, n):
    if not s:
        return []
    else:
        words = s.split()
        result = []
        for word in words:
            consonants = 0
            for letter in word:
                if letter not in "aeiouAEIOU" and letter.isalpha():
                    consonants += 1
            if consonants == n:
                result.append(word)
        return result
