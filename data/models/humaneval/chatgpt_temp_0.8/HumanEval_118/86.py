python
def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    closest_vowel = ''
    distance = None
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            for j in range(i - 1, 0, -1):
                if word[j] in consonants:
                    curr_dist = i - j
                    if distance is None or curr_dist < distance:
                        closest_vowel = word[i]
                        distance = curr_dist
                    break
            if distance == 1:
                break
    return closest_vowel
