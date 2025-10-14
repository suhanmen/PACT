def get_closest_vowel(word):
    vowels = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
    last_consonant = None
    closest_vowel = ""
    for i in range(len(word)-1, 0, -1):
        if word[i] not in vowels and last_consonant != None:
            if closest_vowel == "" or abs(ord(word[i])-ord(last_consonant)) < abs(ord(closest_vowel)-ord(last_consonant)):
                for j in range(i-1, 0, -1):
                    if word[j] in vowels:
                        closest_vowel = word[j]
                        break
            last_consonant = word[i]
        elif word[i] in vowels:
            last_consonant = None
    return closest_vowel
