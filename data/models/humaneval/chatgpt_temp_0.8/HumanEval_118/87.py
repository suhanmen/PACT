def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    right_cons = ""
    for letter in word[::-1]: # reversing the word to search from right side
        if letter not in vowels:
            right_cons += letter
        else:
            break
    if len(right_cons) < 2: # if there are less than 2 consonants from right side, return empty string
        return ""
    else:
        return right_cons[-1] # return the last vowel before the last consonant
