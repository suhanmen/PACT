def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    last_consonant_idx = -1
    result = ""
    
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if last_consonant_idx != -1 and (last_consonant_idx - i) > (len(word) - last_consonant_idx):
                return result
            result = word[i]
        elif word[i].isalpha():
            last_consonant_idx = i
            
    return result
