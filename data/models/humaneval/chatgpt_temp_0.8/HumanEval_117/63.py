def select_words(s, n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    if s == "":
        return result
    else:
        words = s.split()
        for word in words:
            consonants = 0
            for letter in word:
                if letter.lower() not in vowels:
                    consonants += 1
            if consonants == n:
                result.append(word)
        return result
