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
    if not s:
        return []
    
    # Define a helper function to count consonants in a word
    def count_consonants(word):
        count = 0
        for letter in word:
            if letter not in "aeiouAEIOU" and letter.isalpha():
                count += 1
        return count
    
    # Split the string into words
    words = s.split()
    
    # Loop through words and select those with n consonants
    selected_words = []
    for word in words:
        if count_consonants(word) == n:
            selected_words.append(word)
    
    return selected_words
