def get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    last_cons = -1
    closest_vowel = ""
    for i in range(len(word)-2, 0, -1):
        if word[i] not in vowels and word[i-1] in vowels and last_cons != -1:
            closest_vowel = min([v for v in vowels if v > word[last_cons] and v < word[i]], key=lambda x: ord(x)-ord(word[i]))
            break
        elif word[i] not in vowels:
            last_cons = i
    return closest_vowel
