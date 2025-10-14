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
    # Create a list to store the resulting words
    result = []
    # If the input string is empty, return an empty list
    if not s:
        return result
    # Split the string into words
    words = s.split()
    # Iterate over each word
    for word in words:
        # Count the number of consonants in the word
        consonants = 0
        for letter in word:
            if letter.lower() not in ['a', 'e', 'i', 'o', 'u'] and letter.isalpha():
                consonants += 1
        # If the number of consonants in the word is equal to n, add the word to the result
        if consonants == n:
            result.append(word)
    # Return the result
    return result
