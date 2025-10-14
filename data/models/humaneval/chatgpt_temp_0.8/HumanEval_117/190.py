def select_words(s, n):
    if not s:  # if the string is empty
        return []  # return an empty list
    words = s.split()  # split the string into words
    result = []  # initialize an empty list to store the selected words
    for word in words:  # iterate over each word
        consonants = sum(1 for c in word if c.isalpha() and c not in 'AEIOUaeiou')  # count the consonants
        if consonants == n:  # if the word has exactly n consonants
            result.append(word)  # add it to the result list
    return result  # return the list of selected words
