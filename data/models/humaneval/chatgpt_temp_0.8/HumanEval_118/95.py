def get_closest_vowel(word):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word.lower()
    length = len(word)
    
    for i in range(length-2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            return word[i].upper() if word[i].isupper() else word[i]
        
    return ""
