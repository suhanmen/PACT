def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    found_consonant = False
    dist_to_vowel = float('inf')
    closest_vowel = ''
    for i in range(len(word)-2, 0, -1):
        if not found_consonant:
            if word[i] not in vowels:
                found_consonant = True
        else:
            if word[i] in vowels:
                if len(word) - i < dist_to_vowel:
                    dist_to_vowel = len(word) - i
                    closest_vowel = word[i]
                break
    return closest_vowel
