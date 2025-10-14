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
    # Create a list of all consonants
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    # If s is empty, return an empty list
    if not s:
        return []
    # Split the string into words
    words = s.split()
    # Initialize an empty list to store the matching words
    matching_words = []
    # Loop through each word
    for word in words:
        # Count the number of consonants in the word
        num_consonants = 0
        for letter in word:
            if letter.lower() in consonants:
                num_consonants += 1
        # If the word contains exactly n consonants, add it to the matching words list
        if num_consonants == n:
            matching_words.append(word)
    return matching_words
