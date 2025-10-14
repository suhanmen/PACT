def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    word = word[::-1][1:-1] # reverse the word and remove the first and last character
    for i, c in enumerate(word):
        if c in vowels and all(x not in vowels for x in word[i+1:]):
            return c
    return ""
