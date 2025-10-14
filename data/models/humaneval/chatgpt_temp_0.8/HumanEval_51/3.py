def remove_vowels(text):
    vowels = set('aeiouAEIOU')
    return ''.join(c for c in text if c not in vowels)
