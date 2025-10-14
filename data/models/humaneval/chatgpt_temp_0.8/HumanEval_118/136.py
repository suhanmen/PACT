def get_closest_vowel(word):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowels = "aeiouAEIOU"
    last_vowel = ""
    for i in range(len(word)-2, 0, -1):  # iterate from right to left
        if word[i] in vowels:
            if any(c in consonants for c in word[i+1:]):  # check if there are consonants to the right
                if last_vowel == "":  # if this is the first vowel found, return it
                    return word[i]
                else:
                    return last_vowel  # otherwise, return the closest vowel found
            else:
                last_vowel = word[i]
    return ""  # no vowel found
