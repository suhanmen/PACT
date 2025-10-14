def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    if not s:  # if s is empty, return an empty list
        return []
    words = s.split()  # split the string into words
    result = []  # create an empty list for the result
    for word in words:
        consonants = 0  # initialize consonants to 0
        for letter in word:
            if letter.lower() not in "aeiou" and letter.isalpha():
                consonants += 1  # count the consonants in the word
        if consonants == n:
            result.append(word)  # if the word has n consonants, add it to the result list
    return result
