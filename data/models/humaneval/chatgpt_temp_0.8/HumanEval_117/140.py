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
    # Replace all spaces with a unique character to split the string into words
    s = s.replace(" ", "_")
    # Initialize an empty list to store words that meet the criteria
    selected_words = []
    # Split the string into words
    words = s.split("_")
    # Loop through each word
    for word in words:
        # Count the number of consonants in the word
        num_consonants = sum(1 for c in word if c.lower() not in "aeiou")
        # If the number of consonants matches the input n, add the word to the selected_words list
        if num_consonants == n:
            selected_words.append(word)
    # Return the selected_words list
    return selected_words
