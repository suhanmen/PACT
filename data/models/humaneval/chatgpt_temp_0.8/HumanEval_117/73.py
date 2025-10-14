def select_words(s, n):
    if not s:  # if the string s is empty, return an empty list
        return []
    words = s.split()  # split the string into words
    consonants = set("bcdfghjklmnpqrstvwxyz")  # set of consonants
    result = []  # create an empty list to store the result
    for word in words:
        count = 0  # initialize the count of consonants
        for letter in word.lower():  # convert the word to lowercase and iterate over its letters
            if letter in consonants:  # if the letter is a consonant, increment the count
                count += 1
        if count == n:  # if the count of consonants equals n, add the word to the result list
            result.append(word)
    return result
