python
def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    word = word[::-1][1:-1]  # reverse the word and remove first and last characters
    
    for i, c in enumerate(word):
        if c in vowels:
            return c
        elif i > 0 and word[i-1] not in vowels and word[i-1] != c:
            return ''  # no more vowels between two consonants
    return ''  # no vowel found
