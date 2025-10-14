def get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    last_consonant_index = None
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels and word[i - 1] in vowels:
            last_consonant_index = i
            break
    if last_consonant_index is None:
        return ""

    closest_vowel_distance = float("inf")
    closest_vowel = ""
    for i in range(last_consonant_index - 1, 0, -1):
        if word[i] in vowels:
            distance = last_consonant_index - i
            if distance < closest_vowel_distance:
                closest_vowel_distance = distance
                closest_vowel = word[i]
    return closest_vowel
