def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for c in text:
        if c not in vowels:
            result += c
    return result
