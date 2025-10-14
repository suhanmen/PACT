def get_closest_vowel(word):
    vowels = set("AEIOUaeiou")
    word = word[::-1] # reverse the word
    i = 0
    while i < len(word) - 1:
        if word[i] not in vowels and word[i+1] in vowels:
            return word[i+1]
        i += 1
    return ""
