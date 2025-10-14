python
def select_words(s, n):
    # If the input string is empty, return an empty list
    if not s:
        return []
    
    # Define a function to check if a given character is a consonant
    def is_consonant(c):
        return c.lower() not in ['a', 'e', 'i', 'o', 'u', ' ']
    
    # Split the input string into words
    words = s.split()
    
    # Iterate over the words and check if they contain exactly n consonants
    selected_words = []
    for word in words:
        consonant_count = sum([is_consonant(c) for c in word])
        if consonant_count == n:
            selected_words.append(word)
    
    return selected_words
