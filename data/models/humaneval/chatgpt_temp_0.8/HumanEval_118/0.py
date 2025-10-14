def get_closest_vowel(word):
    # Find the last two consonants from the right
    consonants = ""
    for letter in reversed(word[:-1]):
        if letter.lower() not in "aeiou":
            consonants += letter
        else:
            break
    
    # If we didn't find two consonants, return an empty string
    if len(consonants) < 2:
        return ""
    
    # Find the closest vowel between the two consonants
    for letter in reversed(word[:-1]):
        if letter.lower() in "aeiou":
            return letter.upper() if letter.isupper() else letter
        elif letter in consonants:
            break
    
    return ""
