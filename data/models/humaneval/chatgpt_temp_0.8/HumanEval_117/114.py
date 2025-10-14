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
    if not s:  # If the string is empty, return an empty list
        return []
    words = s.split()  # Split the string s into words
    result = []  # Initialize an empty list to hold the result
    for word in words:  # Iterate through each word in the string
        consonant_count = 0  # Initialize a count for consonants in the word
        for letter in word:  # Iterate through each letter in the word
            if letter.lower() not in "aeiou" and letter.isalpha():  # If the letter is a consonant, increment the count
                consonant_count += 1
        if consonant_count == n:  # If the consonant count matches the input value n, add the word to the result list
            result.append(word)
    return result  # Return the result list
