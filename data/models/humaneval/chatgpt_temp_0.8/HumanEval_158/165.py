def find_max(words):
    max_word = ""
    max_count = 0
    
    for word in words:
        # Count the number of unique characters in the word
        unique_count = len(set(word))
        # Check if the word has more unique characters than the current maximum
        if unique_count > max_count:
            max_word = word
            max_count = unique_count
        # If the word has the same number of unique characters as the current maximum
        elif unique_count == max_count:
            # Check if the word comes before the current maximum in lexicographical order
            if word < max_word:
                max_word = word
                
    return max_word
