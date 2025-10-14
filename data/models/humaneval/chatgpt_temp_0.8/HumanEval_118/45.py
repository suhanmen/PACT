def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    right_consonants = ""
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels:
            right_consonants += word[i]
        else:
            return min([c for c in right_consonants], key=lambda c: ord(c))
    return ""
