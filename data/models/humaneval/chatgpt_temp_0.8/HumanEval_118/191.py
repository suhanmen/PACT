def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    # split the word into two parts: before and after the last consonant
    parts = word.rsplit(maxsplit=1)
    if len(parts) < 2:
        return ""  # no consonant found
    # check the second part for the closest vowel before the last consonant
    for i in range(len(parts[1])-1, -1, -1):
        if parts[1][i] in vowels:
            return parts[1][i]  # found a vowel
        elif parts[1][i] in consonants:
            return ""  # no vowel found
    return ""  # no vowel found in the second part
