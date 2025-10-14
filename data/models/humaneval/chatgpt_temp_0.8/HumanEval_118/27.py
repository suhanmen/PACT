def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    reverse_word = word[::-1]
    vowel_index = None
    
    for i, char in enumerate(reverse_word[1:-1]):
        if char in vowels and reverse_word[i+2] in consonants:
            vowel_index = len(word) - i - 2
            break
        
    if vowel_index is None:
        return ""
    else:
        return word[vowel_index]
