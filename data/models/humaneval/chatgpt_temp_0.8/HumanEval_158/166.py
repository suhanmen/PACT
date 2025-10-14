def find_max(words):
    max_unique = 0
    max_word = ""
    
    for word in words:
        unique_chars = set(word)
        num_unique = len(unique_chars)
        
        if num_unique > max_unique:
            max_unique = num_unique
            max_word = word
        elif num_unique == max_unique and word < max_word:
            max_word = word
    
    return max_word
