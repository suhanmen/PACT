def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    indices = [i for i in range(1, len(word)-1) if word[i] not in vowels 
               and word[i-1] in vowels and word[i+1] in vowels]
    if not indices:
        return ""
    closest_vowel_index = min(indices, key=lambda x: abs(x-(len(word)-2)))
    return word[closest_vowel_index]
