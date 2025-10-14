def select_words(s, n):
    if not s:  # if the string s is empty
        return []  # return an empty list
    result = []
    words = s.split()  # split the string into a list of words
    for word in words:
        consonants = 0
        for letter in word:
            if letter.lower() not in 'aeiou':  # if the letter is not a vowel
                consonants += 1  # increment the consonant count
        if consonants == n:  # if the word contains exactly n consonants
            result.append(word)  # add the word to the result list
    return result
