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
    # create a list of all the words in the string s
    words = s.split()

    # create an empty list to store the words that meet the criteria
    result = []

    # iterate through each word in the list of words
    for word in words:
        # count the number of consonants in the word
        consonant_count = sum(1 for letter in word if letter.lower() not in 'aeiou')

        # if the consonant count matches the given n, add the word to the result list
        if consonant_count == n:
            result.append(word)

    return result
