def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
  
    last_consonant_index = len(word)-1
    while last_consonant_index >= 0 and word[last_consonant_index] in vowels:
        last_consonant_index -= 1

    if last_consonant_index < 1:
        return ""

    for i in range(last_consonant_index-1, 0, -1):
        if word[i] in vowels and word[i-1] in consonants and word[i+1] in consonants:
            return word[i]

    return ""
