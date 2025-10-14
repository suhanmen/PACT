def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            for j in range(i-1, 0, -1):
                if word[j] in consonants:
                    for k in range(j-1, 0, -1):
                        if word[k] in vowels:
                            return word[i]
    return ""
